import copy
import math
from dataclasses import dataclass
from enum import Enum


class Player(Enum):
    human = "human"
    computer = "computer"


class GameWinner(Enum):
    human = "human"
    computer = "computer"
    tie = "tie"


class Pattern(Enum):
    cross = "X"
    zero = "O"
    blank = " "


@dataclass
class Board:
    board: list[Pattern]
    player: Player
    current_move: Pattern
    first_move: Player
    game_over: bool = False

    def available_moves(self):
        return [i for i, p in enumerate(self.board) if p == Pattern.blank]


def print_board(board: Board):
    for i in range(3):
        for j in range(3):
            print(board.board[3 * i + j].value, end="|" if j != 2 else "\n")
        if i != 2:
            print("-" * 5)


def minimax(board, maximizing):
    state = game_over(board)
    if state is not None:
        if state == GameWinner.computer:
            return 1, None
        elif state == GameWinner.human:
            return -1, None
        elif state == GameWinner.tie:
            return 0, None

    best_val = -math.inf if maximizing else math.inf
    best_move = None

    for move in board.available_moves():
        new_board = copy.deepcopy(board)
        do_move(new_board, move)
        val, _ = minimax(new_board, not maximizing)
        if maximizing and val > best_val or not maximizing and val < best_val:
            best_val, best_move = val, move

    return best_val, best_move


def game_over(board: Board):
    for i in range(0, 9, 3):
        if (
            board.board[i] == board.board[i + 1]
            and board.board[i] == board.board[i + 2]
            and board.board[i] != Pattern.blank
        ):
            if board.board[i] == Pattern.cross:
                return board.first_move
            else:
                return (
                    GameWinner.computer
                    if board.first_move == Player.human
                    else GameWinner.human
                )

    for i in range(3):
        if (
            board.board[i] == board.board[i + 3]
            and board.board[i] == board.board[i + 6]
            and board.board[i] != Pattern.blank
        ):
            if board.board[i] == Pattern.cross:
                return board.first_move
            else:
                return (
                    GameWinner.computer
                    if board.first_move == Player.human
                    else GameWinner.human
                )

    if (
        board.board[0] == board.board[4]
        and board.board[0] == board.board[8]
        and board.board[0] != Pattern.blank
    ):
        if board.board[0] == Pattern.cross:
            return board.first_move
        else:
            return (
                GameWinner.computer
                if board.first_move == Player.human
                else GameWinner.human
            )

    if (
        board.board[2] == board.board[4]
        and board.board[2] == board.board[6]
        and board.board[2] != Pattern.blank
    ):
        if board.board[2] == Pattern.cross:
            return board.first_move
        else:
            return (
                GameWinner.computer
                if board.first_move == Player.human
                else GameWinner.human
            )

    if all(p != Pattern.blank for p in board.board):
        return GameWinner.tie

    return None


def do_move(board: Board, move: int):
    board.board[move] = board.current_move
    board.player = Player.computer if board.player == Player.human else Player.human
    board.current_move = (
        Pattern.cross if board.current_move == Pattern.zero else Pattern.zero
    )


def get_move(board: Board):
    print_board(board)
    print(f"Current move by {board.player.value}, place a {board.current_move.value}")
    can_move = False
    move = None
    while not can_move:
        move = int(input("Move to where: "))
        if board.board[move] != Pattern.blank:
            print("Can only place at blank spots")
        else:
            can_move = True
    if can_move and move is not None:
        do_move(board, move)
        state = game_over(board)
        if state is not None:
            board.game_over = True
            print_board(board)
            print(f"Game is won by {state.value}")


def main():
    player = input("First move goes to (H/C): ").upper()
    board = Board(
        [Pattern.blank] * 9,
        Player.human if player == "H" else Player.computer,
        Pattern.cross,
        Player.human if player == "H" else Player.computer,
    )

    while True:
        if board.game_over:
            break
        if board.player == Player.human:
            get_move(board)
        else:
            _, move = minimax(board, True)
            if move is not None:
                do_move(board, move)
                state = game_over(board)
                if state is not None:
                    board.game_over = True
                    print_board(board)
                    print(f"Game is won by {state.value}")


if __name__ == "__main__":
    main()
