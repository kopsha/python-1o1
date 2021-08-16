"""
Rock Scissor Paper is a well known and fun game
Just sellecrt R, S or P and have fun
"""

import sys
import random

"""<< [r]ock [p]aper [s]cissor or quit << p

 >> round   3
 >> [player]     rock   vs   paper    [computer] <<
 ..:: computer wins ::..  reason: paper covers rock.
 >>   1 (50.00 %)  --  (50.00 %)   1"""


def play_rock_scissors_paper():
    valid_inputs = ["r", "s", "p"]
    evaluation = {"pr": 1, "rp": -1, "sp": 1, "ps": -1, "rs": 1, "sr": -1}
    reason_definition = {"pr": "paper covers rock",
                         "rp": "paper covers rock",
                         "sp": "scissors cuts paper",
                         "ps": "scissors cuts paper",
                         "rs": "rock breaks scissors",
                         "sr": "rock breaks scissors",
                         }
    full_choice = {"p": "paper", "r": "rock,", "s": "scissors"}
    player_input = ""
    round_number = 0
    user_wins = 0
    computer_wins = 0
    draws = 0

    while player_input.lower() != "q":
        player_input = input("<< [r]ock [p]aper [s]cissor or quit: ")
        if player_input in ["q"]:
            break
        if player_input not in full_choice.keys():
            print("Please use only indicated letters")
            continue

        round_number += 1
        computer_input = random.choice(list(full_choice))
        print("round  ", round_number)
        print(f">> [player]   {full_choice[player_input]}  vs  {full_choice[computer_input]}   [computer] <<")

        result = evaluation.get(player_input + computer_input, 0)
        if result > 0:
            winner = "player"
            user_wins += 1
        elif result < 0:
            winner = "computer"
            computer_wins += 1
        else:
            winner = "nobody"
            draws += 1
        won_games = (round_number - draws) or 1
        print(f"..:: {winner} wins ::.. reason: {reason_definition.get(player_input + computer_input, 'it is a draw')}")
        print(f" {user_wins} ({(user_wins/won_games) * 100:.2f}  %)  --  ({(computer_wins/won_games) * 100:.2f} %)   {computer_wins}")


def main():
    play_rock_scissors_paper()

main()