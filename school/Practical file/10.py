# WAP to make a rock scissor and paper game

import random
inp = input("Enter rock(r), paper(p), or scissors(s): ").lower()
game_choice = None
rand_int = random.randint(1,3)
if rand_int == 1:
    game_choice = "rock"
elif rand_int == 2:
    game_choice = "scissor"
else:
    game_choice = "paper"
print(f"Computer choose {game_choice}")

if game_choice[0] == 'r' and inp == 'p':
    print("Player wins")
elif game_choice[0] == 's' and inp == 'r':
    print("Player wins")
elif game_choice[0] == 'p' and inp == 's':
    print("Player wins")
elif inp == 'r' and game_choice[0] == 'p':
    print("Computer wins")
elif inp == 's' and game_choice[0] == 'r':
    print("Computer wins")
elif inp == 'p' and game_choice[0] == 's':
    print("Computer wins")
else:
    print("Tie")
