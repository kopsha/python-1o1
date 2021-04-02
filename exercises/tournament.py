"""
Tally the results of a small football competition.

Based on an input file containing which team played against which and what the
outcome was, create a file with a table like this:

Team                           | MP |  W |  D |  L |  P
Dortmund                       |  3 |  2 |  1 |  0 |  7
Barcelona                      |  3 |  2 |  0 |  1 |  6
Juventus                       |  3 |  1 |  0 |  2 |  3
Chelsea                        |  3 |  0 |  1 |  2 |  1


What do those abbreviations mean?

MP: Matches Played
W: Matches Won
D: Matches Drawn (Tied)
L: Matches Lost
P: Points

A win earns a team 3 points. A draw earns 1. A loss earns 0.

The outcome should be ordered by points, descending. In case of a tie, teams are
ordered alphabetically.



Input
^^^^^

Your tallying program will receive input that looks like:

    Barcelona;Juventus;win
    Dortmund;Chelsea;draw
    Dortmund;Barcelona;win
    Chelsea;Juventus;loss
    Juventus;Dortmund;loss
    Barcelona;Chelsea;win


The result of the match refers to the first team listed.
So the line:
    Barcelona;Juventus;win
Means that the Barcelona beat the Juventus.
And this line
    Chelsea;Juventus;loss
Means that the Juventus beat the Chelsea.

And this line:
    Dortmund;Chelsea;draw
Means that the Dortmund and Chelsea tied.
"""

import sys

text = """
Barcelona;Juventus;win
Dortmund;Chelsea;draw
Dortmund;Barcelona;win
Chelsea;Juventus;loss
Juventus;Dortmund;loss
Barcelona;Chelsea;win
"""


def sum_tuple(left, right):
    """returns a new tuple with the sum of tuples element by element"""
    return tuple(sum(value) for value in zip(left, right))


def print_table(name_team, played_matches, won, draw, loss, points, separator="|"):
    """composes a string for printing as a table"""
    my_output = (
        "{:<30}".format(name_team)
        + separator
        + "{:^4}".format(played_matches)
        + separator
        + "{:^4}".format(won)
        + separator
        + "{:^4}".format(draw)
        + separator
        + "{:^4}".format(loss)
        + separator
        + "{:^4}".format(points)
        + "\n"
    )
    return my_output


def tally_tournament(text):
    """given all lines, computes the tournament scores and returns a dict
    result dictionary:
    "Dortmund": (3,  2,  1,  0,  7),
    """
    if not isinstance(text, str):
        raise TypeError("Tournament data must be a string (text).")

    lines = text.split()
    stats = {}

    for line in lines:
        home_team, away_team, result = line.split(";")

        if result == "win":
            current_home = (1, 1, 0, 0, 3)
            current_away = (1, 0, 0, 1, 0)
        elif result == "draw":
            current_home = (1, 0, 1, 0, 1)
            current_away = (1, 0, 1, 0, 1)
        else:
            current_home = (1, 0, 0, 1, 0)
            current_away = (1, 1, 0, 0, 3)

        stats[home_team] = sum_tuple(
            stats.get(home_team, (0, 0, 0, 0, 0)), current_home
        )
        stats[away_team] = sum_tuple(
            stats.get(away_team, (0, 0, 0, 0, 0)), current_away
        )

    return stats


def pretty_tournament(scores):
    """given the scores, will format the tables"""
    if not scores:
        raise TypeError("Dictionary is empty")

    composed_output = print_table("Team", "MP", "W", "D", "L", "P")
    points_cumulus = {stats[-1]: team for team, stats in scores.items()}
    for key in sorted(points_cumulus.keys(), reverse=True):
        played_matches, won, draw, loss, points = scores[points_cumulus[key]]
        composed_output += print_table(
            points_cumulus[key], played_matches, won, draw, loss, points
        )

    return composed_output


def main():
    file_name = "tournament_input.txt"
    file_content = ""

    try:
        with open(file_name) as file:
            file_content = file.read()
    except FileNotFoundError as error:
        print(error)
        sys.exit(-1)

    print(" >> Given input file")
    print(file_content)

    data = tally_tournament(file_content)
    pretty_stats = pretty_tournament(data)

    print(" >> Tallied tournament data:", data)
    print(" >> Tournament table:")
    print(pretty_stats)

    file_output_name = "pretty_stats.txt"

    try:
        with open(file_output_name, "w") as file:
            file.write(pretty_stats)
    except FileNotFoundError as error:
        print(error)
        sys.exit(-1)

    print("=" * 25)


if __name__ == "__main__":
    main()
