"""
Rock Scissor Paper is a well known and fun game
Just sellecrt R, S or P and have fun
"""

import sys
import random


PLAYER1 = 0
PLAYER2 = 1
TIE = 2
valid_inputs = ["r", "s", "p"]
evaluation = {
    "pr": PLAYER1,
    "rp": PLAYER2,
    "ps": PLAYER2,
    "sp": PLAYER1,
    "rs": PLAYER1,
    "sr": PLAYER2,
}


def get_user_input():
    user_input = ""
    while user_input not in valid_inputs + ["q"]:
        user_input = input("<< [r]ock [p]aper [s]cissor or [q]uit: ").lower()

    return user_input


def get_random_input():
    return random.choice(valid_inputs)


def calculate_winner(player1, player2):
    return evaluation.get(player1 + player2, TIE)


def print_result(winner, player1, player2, counters):
    full_choice = {"p": "paper", "r": "rock", "s": "scissors"}
    display_winner = {PLAYER1: "player", PLAYER2: "computer", TIE: "nobody"}
    reasons = {
        "pr": "paper covers rock.",
        "rp": "paper covers rock.",
        "ps": "scissors cuts paper.",
        "sp": "scissors cuts paper.",
        "rs": "rock breaks scissors.",
        "sr": "rock breaks scissors.",
    }

    print(
        f"[player]    {full_choice[player1]}   vs   {full_choice[player2]}     [computer] <<"
    )
    rounds = (counters[PLAYER1] + counters[PLAYER2]) or 1

    p1_wins_percent = 100 * counters[PLAYER1] / rounds
    p2_wins_percent = 100 * counters[PLAYER2] / rounds

    print(f"round {sum(counters)}")
    print(
        f"..:: {display_winner[winner]} wins ::.. reason: {reasons.get(player1 + player2, 'its a draw')}"
    )
    print(
        f">>   {counters[PLAYER1]} ({p1_wins_percent:.2f}%)  --  ({p2_wins_percent:.2f}%)   {counters[PLAYER2]}"
    )


def main():
    player1 = ""
    counters = [0, 0, 0]  # [player1_wins, player2_wins, ties]
    while True:

        player1 = get_user_input()
        if player1 == "q":
            break
        
        player2 = get_random_input()

        winner = calculate_winner(player1, player2)
        counters[winner] += 1

        print_result(winner, player1, player2, counters)


if __name__ == "__main__":
    main()
