"""
Establish which kind of Poker combination is present in a deck of five cards.
Every card is a string containing the card value (with the upper-case initial
for face-cards) and the lower-case initial for suits, as in the examples below:

"Ah" ➞ Ace of hearts
"Ks" ➞ King of spades
"3d" ➞ Three of diamonds
"Qc" ➞ Queen of clubs

There are 10 different combinations.

Here's the list, in decreasing order of importance:

Name            Description
Royal Flush     A, K, Q, J, 10, all with the same suit.
Straight Flush  Five cards in sequence, all with the same suit.
Four of a Kind  Four cards of the same rank.
Full House      Three of a Kind with a Pair.
Flush           Any five cards of the same suit, not in sequence.
Straight        Five cards in a sequence, but not of the same suit.
Three of a Kind Three cards of the same rank.
Two Pair        Two different Pair.
Pair            Two cards of the same rank.
High Card       No other valid combination.


Given a list hand containing five strings being the cards, implement a function
that returns a string with the name of the highest combination obtained,
accordingly to the table above.

Examples
poker_hand_ranking(["10h", "Jh", "Qh", "Ah", "Kh"]) ➞ "Royal Flush"
poker_hand_ranking(["3h", "5h", "Qs", "9h", "Ad"]) ➞ "High Card"
poker_hand_ranking(["10s", "10c", "8d", "10d", "10h"]) ➞ "Four of a Kind"

"""
from collections import namedtuple

Card = namedtuple("Card", ["rank", "color"])


def poker_hand_ranking(raw_hand):
    high_cards = {"J": 11, "Q": 12, "K": 13, "A": 14}
    hand = []
    result = ""

    for raw_card in raw_hand:
        color = raw_card[-1]
        rank = int(high_cards.get(raw_card[:-1], raw_card[:-1]))
        hand.append(Card(rank, color))

    hand.sort(key=lambda x: x.rank)
    print("hand", hand)

    colors = {card.color for card in hand}
    # preparations
    is_flush = False
    if len(colors) == 1:
        is_flush = True

    aces = {card.rank for card in hand if card.rank == 11}
    is_ace = False
    if len(aces) > 0:
        is_ace = True

    # are consecutive cards
    are_consecutive = [
        (right.rank - left.rank) == 1 for left, right in zip(hand[:-1], hand[1:])
    ]
    is_straight = all(are_consecutive)

    # cards with same rank
    cards = {}
    for card in hand:
        cards[card.rank] = cards.get(card.rank, 0) + 1
    cards_same_rank = max(cards.values())

    # final evaluation
    if len(cards) == 5:
        result = "High Card"
    elif len(cards) == 4:
        result = "Pair"
    elif len(cards) == 3:
        if cards_same_rank == 3:
            result = "Three of a Kind"
        else:
            result = "Two Pair"
    elif len(cards) == 2:
        if cards_same_rank == 4:
            result = "Four of a Kind"
        else:
            result = "Full House"

    if is_flush and is_straight and is_ace:
        result = "Royal Flush"
    elif is_flush and is_straight:
        result = "Straight Flush"
    elif is_straight:
        result = "Straight"
    elif is_flush:
        result = "Flush"

    return result


def test_poker_hand_ranking():
    assert poker_hand_ranking(["10h", "Jh", "Qh", "Ah", "Kh"]) == "Royal Flush"
    assert poker_hand_ranking(["3h", "5h", "Qs", "9h", "Ad"]) == "High Card"
    assert poker_hand_ranking(["10s", "10c", "8d", "10d", "10h"]) == "Four of a Kind"
    assert poker_hand_ranking(["4h", "9s", "2s", "2d", "Ad"]) == "Pair"
    assert poker_hand_ranking(["10s", "9s", "8s", "6s", "7s"]) == "Straight Flush"
    assert poker_hand_ranking(["10c", "9c", "9s", "10s", "9h"]) == "Full House"
    assert poker_hand_ranking(["8h", "2h", "8s", "3s", "3c"]) == "Two Pair"
    assert poker_hand_ranking(["Jh", "9h", "7h", "5h", "2h"]) == "Flush"
    assert poker_hand_ranking(["Ac", "Qc", "As", "Ah", "2d"]) == "Three of a Kind"
    assert poker_hand_ranking(["Ad", "Kd", "Qd", "Jd", "9d"]) == "Flush"
    assert poker_hand_ranking(["10h", "Jh", "Qs", "Ks", "Ac"]) == "Straight"
    assert poker_hand_ranking(["3h", "8h", "2s", "3s", "3d"]) == "Three of a Kind"
    assert poker_hand_ranking(["4h", "Ac", "4s", "4d", "4c"]) == "Four of a Kind"
    assert poker_hand_ranking(["3h", "8h", "2s", "3s", "2d"]) == "Two Pair"
    assert poker_hand_ranking(["8h", "8s", "As", "Qh", "Kh"]) == "Pair"
    assert poker_hand_ranking(["Js", "Qs", "10s", "Ks", "As"]) == "Royal Flush"
    assert poker_hand_ranking(["Ah", "3s", "4d", "Js", "Qd"]) == "High Card"
