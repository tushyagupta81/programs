import itertools
import os
import random
from datetime import datetime, timedelta

import flappy_bird_gymnasium
import gymnasium as gym
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import torch
import yaml
from torch import nn, unsqueeze

from app.dqn import DQN
from app.experience_replay import ReplayMemory

# For printing date and time
DATE_FORMAT = "%m-%d %H:%M:%S"

# Directory for saving run info
RUNS_DIR = "runs"
os.makedirs(RUNS_DIR, exist_ok=True)

# 'Agg': used to generate plots as images and save them to a file instead of rendering to screen
matplotlib.use("Agg")

# device = "cuda" if torch.cuda.is_available() else "cpu"
device = "cpu"


class Agent:
    def __init__(self, hyperparams_set):
        with open("hyperparams.yaml", "r") as f:
            all_hyperparams = yaml.safe_load(f)
            hyperparams = all_hyperparams[hyperparams_set]

        self.hyperparameter_set = hyperparams_set

        self.env_id = hyperparams["env_id"]
        self.replay_memory_size = hyperparams["replay_memory_size"]
        self.mini_batch_size = hyperparams["mini_batch_size"]
        self.epsilon_init = hyperparams["epsilon_init"]
        self.epsilon_decay = hyperparams["epsilon_decay"]
        self.epsilon_min = hyperparams["epsilon_min"]
        self.network_sync_rate = hyperparams["network_sync_rate"]
        self.learning_rate = hyperparams["learning_rate"]
        self.discount_factor_g = hyperparams["discount_factor_g"]
        self.stop_on_reward = hyperparams["stop_on_reward"]
        self.fc1_nodes = hyperparams["fc1_nodes"]
        self.enable_double_dqn = hyperparams["enable_double_dqn"]
        self.enable_dueling_dqn = hyperparams["enable_dueling_dqn"]
        self.env_make_params = hyperparams.get("env_make_params", {})
        self.loss_fn = nn.MSELoss()

        # Path to Run info
        self.LOG_FILE = os.path.join(RUNS_DIR, f"{self.hyperparameter_set}.log")
        self.MODEL_FILE = os.path.join(RUNS_DIR, f"{self.hyperparameter_set}.pt")
        self.GRAPH_FILE = os.path.join(RUNS_DIR, f"{self.hyperparameter_set}.png")

    def run(self, is_training=True, render=False):
        if is_training:
            start_time = datetime.now()
            last_graph_update_time = start_time

            log_message = f"{start_time.strftime(DATE_FORMAT)}: Training starting..."
            print(log_message)
            with open(self.LOG_FILE, "w") as file:
                file.write(log_message + "\n")

        env = gym.make(
            self.env_id, render_mode="human" if render else None, **self.env_make_params
        )

        num_actions = env.action_space.n  # pyright: ignore[reportAttributeAccessIssue]
        num_states = (
            env.observation_space.shape[0]
            if env.observation_space.shape is not None
            else 12
        )

        policy_dqn = DQN(
            num_states, num_actions, self.fc1_nodes, self.enable_dueling_dqn
        ).to(device)

        if is_training:
            memory = ReplayMemory(self.replay_memory_size)
            epsilon = self.epsilon_init
            epsilon_history = [epsilon]

            target_dqn = DQN(
                num_states, num_actions, self.fc1_nodes, self.enable_dueling_dqn
            ).to(device)
            target_dqn.load_state_dict(policy_dqn.state_dict())
            step_count = 0

            self.optimizer = torch.optim.Adam(
                policy_dqn.parameters(), lr=self.learning_rate
            )
            best_reward = -999
        else:
            policy_dqn.load_state_dict(torch.load(self.MODEL_FILE))
            policy_dqn.eval()

        rewards_pre_epi = []

        for episode in itertools.count():
            state, _ = env.reset()
            state = torch.tensor(state, dtype=torch.float, device=device)

            terminated = False
            episode_reward = 0.0
            while not terminated and episode_reward < self.stop_on_reward:
                # Next action:
                # (feed the observation to your agent here)
                if is_training and random.random() < epsilon:  # pyright: ignore[reportPossiblyUnboundVariable]
                    action = env.action_space.sample()
                else:
                    with torch.no_grad():
                        action = policy_dqn(state.unsqueeze(0)).squeeze().argmax()

                # Processing:
                new_state, reward, terminated, _, _ = env.step(action.item())

                episode_reward += float(reward)

                new_state = torch.tensor(new_state, dtype=torch.float, device=device)
                reward = torch.tensor(reward, dtype=torch.float, device=device)

                if is_training:
                    memory.append((state, action, new_state, reward, terminated))  # pyright: ignore[reportPossiblyUnboundVariable]
                    step_count += 1  # pyright: ignore[reportPossiblyUnboundVariable]

                state = new_state

            rewards_pre_epi.append(episode_reward)

            if is_training:
                if episode_reward > best_reward:  # pyright: ignore[reportPossiblyUnboundVariable]
                    log_message = f"{datetime.now().strftime(DATE_FORMAT)}: New best reward {episode_reward:0.1f} ({(episode_reward - best_reward) / best_reward * 100:+.1f}%) at episode {episode}, saving model..."  # pyright: ignore[reportPossiblyUnboundVariable]
                    print(log_message)
                    with open(self.LOG_FILE, "a") as file:
                        file.write(log_message + "\n")

                    torch.save(policy_dqn.state_dict(), self.MODEL_FILE)
                    best_reward = episode_reward

                # Update graph every x seconds
                current_time = datetime.now()
                if current_time - last_graph_update_time > timedelta(seconds=10):  # pyright: ignore[reportPossiblyUnboundVariable]
                    self.save_graph(rewards_pre_epi, epsilon_history)  # pyright: ignore[reportPossiblyUnboundVariable]
                    last_graph_update_time = current_time

                if len(memory) > self.mini_batch_size:  # pyright: ignore[reportPossiblyUnboundVariable]
                    mini_batch = memory.sample(self.mini_batch_size)  # pyright: ignore[reportPossiblyUnboundVariable]

                    self.optimize(mini_batch, policy_dqn, target_dqn)  # pyright: ignore[reportPossiblyUnboundVariable]

                    epsilon = max(self.epsilon_min, epsilon * self.epsilon_decay)  # pyright: ignore[reportPossiblyUnboundVariable]
                    epsilon_history.append(epsilon)  # pyright: ignore[reportPossiblyUnboundVariable]

                    if step_count > self.network_sync_rate:  # pyright: ignore[reportPossiblyUnboundVariable]
                        target_dqn.load_state_dict(policy_dqn.state_dict())  # pyright: ignore[reportPossiblyUnboundVariable]
                        step_count = 0

        env.close()

    def save_graph(self, rewards_per_episode, epsilon_history):
        # Save plots
        fig = plt.figure(1)

        # Plot average rewards (Y-axis) vs episodes (X-axis)
        mean_rewards = np.zeros(len(rewards_per_episode))
        for x in range(len(mean_rewards)):
            mean_rewards[x] = np.mean(rewards_per_episode[max(0, x - 99) : (x + 1)])
        plt.subplot(121)  # plot on a 1 row x 2 col grid, at cell 1
        # plt.xlabel('Episodes')
        plt.ylabel("Mean Rewards")
        plt.plot(mean_rewards)

        # Plot epsilon decay (Y-axis) vs episodes (X-axis)
        plt.subplot(122)  # plot on a 1 row x 2 col grid, at cell 2
        # plt.xlabel('Time Steps')
        plt.ylabel("Epsilon Decay")
        plt.plot(epsilon_history)

        plt.subplots_adjust(wspace=1.0, hspace=1.0)

        # Save plots
        fig.savefig(self.GRAPH_FILE)
        plt.close(fig)

    def optimize(self, mini_batch, policy_dqn, target_dqn):
        states, actions, new_states, rewards, terminations = zip(*mini_batch)
        states = torch.stack(states)
        actions = torch.tensor(actions, dtype=torch.int64, device=device)
        new_states = torch.stack(new_states)
        rewards = torch.stack(rewards)
        terminations = torch.tensor(terminations).float().to(device)

        with torch.no_grad():
            if self.enable_double_dqn:
                best_actions_from_policy = policy_dqn(new_states).argmax(dim=1)
                target_q = (
                    rewards
                    + (1 - terminations)
                    * self.discount_factor_g
                    * target_dqn(new_states)
                    .gather(dim=1, index=best_actions_from_policy.unsqueeze(dim=1))
                    .squeeze()
                )
            else:
                target_q = (
                    rewards
                    + (1 - terminations)
                    * self.discount_factor_g
                    * target_dqn(new_states).max(dim=1)[0]
                )

        current_q = (
            policy_dqn(states).gather(dim=1, index=actions.unsqueeze(dim=1)).squeeze()
        )

        loss = self.loss_fn(current_q, target_q)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
