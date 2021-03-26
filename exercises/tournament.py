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


def tally_tournament(text):
    """given all lines, computes the tournament scores and returns a dict"""
    return {}

def pretty_tournament(scores):
    """given the scores, will format the tables"""
    return ''

def main():
    file_name = "tournament_input.txt"
    file_content = ''  # TODO: fill this in...

    print(" >> Given input file")
    print(file_content)

    data = tally_tournament(file_content)
    pretty_stats = pretty_tournament(data)

    print(" >> Tallied tournament data:", data)
    print(" >> Tournament table:")
    print(pretty_stats)
    # TODO: also print to file

    print("="*25)


if __name__ == '__main__':
    main()
