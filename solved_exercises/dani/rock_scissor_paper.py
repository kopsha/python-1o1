"""
Rock Scissor Paper is a well known and fun game
Just sellecrt R, S or P and have fun
"""

import sys
import random


def division(number, divisor):
    return number / divisor if divisor else 0


def rsp_game():
    """given a value for r(ock), s(cissor) or p(aper) from keyboard
    the function will generate a random value to be compared with user choice.
    """

    player_input = ""
    evaluation = {"pr": 1, "rp": -1, "ps": -1, "sp": 1, "rs": 1, "sr": -1}
    full_choice = {"p": "paper", "r": "rock", "s": "scissors"}
    reasons = {
        "pr": "paper covers rock.",
        "rp": "paper covers rock.",
        "ps": "scissors cuts paper.",
        "sp": "scissors cuts paper.",
        "rs": "rock breaks scissors.",
        "sr": "rock breaks scissors.",
    }
    rounds = 0
    player_wins = 0
    computer_wins = 0
    ties = 0
    while player_input.lower() != "q":
        # Read Input
        player_input = input("<< [r]ock [p]aper [s]cissor or q[uit]")

        # Validate input
        if player_input in ["q"]:
            break

        if player_input not in full_choice.keys():
            print("Please use only indicated letters")
            continue
        rounds += 1
        # randomize
        computer_input = random.choice(list(full_choice))
        print(
            f"[player]    {full_choice[player_input]}   vs   {full_choice[computer_input]}     [computer] <<"
        )

        result = evaluation.get(player_input + computer_input, 0)
        if result > 0:
            winner = "player"
            player_wins += 1
        elif result < 0:
            winner = "computer"
            computer_wins += 1
        else:
            winner = "nobody"
            ties += 1
        player_wins_percent = 100 * division(player_wins, rounds - ties)
        computer_wins_percent = 100 * division(computer_wins, rounds - ties)
        print(f"round {rounds}")
        print(
            f"..:: {winner} wins ::.. reason: {reasons.get(player_input + computer_input, 'its a draw')}"
        )
        print(
            f">>   {player_wins} ({round(player_wins_percent, 2)}%)  --  ({round(computer_wins_percent, 2)} %)   {computer_wins}"
        )


def main():
    rsp_game()


if __name__ == "__main__":
    main()
