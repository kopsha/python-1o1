"""
Given a knapsack with a certain weight capacity, fill it with loot from a list
of items to achieve the highest value possible.

The function takes two parameters: an integer specifying the maximum weight the
knapsack can hold, and a list of dictionary items to choose from. Each item has
a name, a weight, and a value. The total weight of all chosen items cannot
exceed the capacity of the knapsack.

The function should return a dictionary containing the capacity of the bag, a
list of items that were added to the bag (in the same order that they were
given), the total weight of those items, and the total value of the items.

Example
knapsack(0, items) => {
  "capacity": 0,
  "items": [],
  "weight": 0,
  "value": 0
}
"""

from collections import namedtuple, deque
from itertools import combinations
from datetime import datetime
import timeit

from pprint import pprint

SackItem = namedtuple("SackItem", ["name", "weight", "value"])


def iter_knapsack(capacity, items):
    reduced_items = [SackItem(**i) for i in items if i["weight"] <= capacity]

    best_value = 0
    best_weight = 0
    best_items = []

    for k in reversed(range(1, len(reduced_items) + 1)):
        for proposal in combinations(reduced_items, k):
            p_weigth = sum(p.weight for p in proposal)
            if p_weigth > capacity:
                continue

            p_value = sum(p.value for p in proposal)
            if p_value > best_value:
                best_value = p_value
                best_weight = p_weigth
                best_items = [p._asdict() for p in proposal]

    return {
        "capacity": capacity,
        "items": best_items,
        "weight": best_weight,
        "value": best_value,
    }



def back_knapsack(capacity, all_items):
    items = [SackItem(**i) for i in all_items if i["weight"] <= capacity]
    n = len(items)

    # print("--" * 20)
    # print([(x["name"], x["weight"], x["value"]) for x in all_items])

    best_value = 0
    best_weight = 0
    best_solution = []
    remaining = tuple(range(n))

    stack = deque([ ((), remaining) ])
    # pprint(stack)

    while stack:
        # print(" >> stack")
        # pprint(stack)
        solution, moves = stack.popleft()
        weight = sum(items[x].weight for x in solution)
        left_capacity = capacity - weight

        valid_moves = [m for m in moves if items[m].weight <= left_capacity]
        for i, m in enumerate(valid_moves):
            stack.append(( solution + (m,), tuple(valid_moves[i+1:]) ))


        if not valid_moves:

            value = sum(items[x].value for x in solution)
            if value > best_value:
                best_value = value
                best_weight = weight
                best_solution = solution
                # print(" >> best", best_weight, best_value, [items[x].name for x in best_solution])

    return {
        "capacity": capacity,
        "items": [items[x]._asdict() for x in best_solution],
        "weight": best_weight,
        "value": best_value,
    }



def recursive_knapsak(capacity, items):

    max_value = 0
    max_weight = 0
    max_valued_packed = []

    if len(items) == 0:
        return max_value, max_valued_packed, max_weight

    for i, item in enumerate(items):
        if item["weight"] > capacity:
            continue

        value, packed, weight = recursive_knapsak(
            capacity - item["weight"], items[i + 1 :]
        )
        if value + item["value"] >= max_value:
            max_value = value + item   ["value"]
            max_valued_packed = [item  ] + packed
            max_weight = weight + item ["weight"]

    return max_value, max_valued_packed, max_weight


def recur_knapsack(capacity, items):
    knapsack_items = []
    items_weight = 0
    items_value = 0

    items_value, knapsack_items, items_weight = recursive_knapsak(capacity, items)

    return {
        "capacity": capacity,
        "items": knapsack_items,
        "weight": items_weight,
        "value": items_value,
    }


def test_knapsack(knapsack):

    items3 = [
        {"name": "desk lamp", "weight": 1, "value": 1000},
        {"name": "beach towel", "weight": 29, "value": 900},
        {"name": "textbook", "weight": 1, "value": 899},
        {"name": "wall clock", "weight": 1, "value": 850},
    ]
    assert knapsack(30, items3) == {
        "capacity": 30,
        "items": [
            {"name": "desk lamp", "weight": 1, "value": 1000},
            {"name": "textbook", "weight": 1, "value": 899},
            {"name": "wall clock", "weight": 1, "value": 850},
        ],
        "weight": 3,
        "value": 2749,
    }

    items = [
        {"name": "desk lamp", "weight": 2, "value": 12},
        {"name": "beach towel", "weight": 1, "value": 10},
        {"name": "textbook", "weight": 3, "value": 20},
        {"name": "wall clock", "weight": 2, "value": 15},
        {"name": "frozen dinners", "weight": 10, "value": 50},
        {"name": "tablet", "weight": 7, "value": 1400},
        {"name": "smartphone", "weight": 1, "value": 200},
        {"name": "paper", "weight": 2, "value": 5},
        {"name": "laser printer", "weight": 25, "value": 400},
        {"name": "shoes", "weight": 1, "value": 79},
        {"name": "medicine", "weight": 1, "value": 17},
        {"name": "decorative cushion", "weight": 1, "value": 11},
        {"name": "gold necklace", "weight": 1, "value": 2500},
        {"name": "toaster oven", "weight": 5, "value": 129},
    ]
    assert knapsack(0, items) == {"capacity": 0, "items": [], "weight": 0, "value": 0}
    assert knapsack(1, items) == {
        "capacity": 1,
        "items": [{"name": "gold necklace", "weight": 1, "value": 2500}],
        "weight": 1,
        "value": 2500,
    }
    assert knapsack(2, items) == {
        "capacity": 2,
        "items": [
            {"name": "smartphone", "weight": 1, "value": 200},
            {"name": "gold necklace", "weight": 1, "value": 2500},
        ],
        "weight": 2,
        "value": 2700,
    }
    assert knapsack(5, items) == {
        "capacity": 5,
        "items": [
            {"name": "smartphone", "weight": 1, "value": 200},
            {"name": "shoes", "weight": 1, "value": 79},
            {"name": "medicine", "weight": 1, "value": 17},
            {"name": "decorative cushion", "weight": 1, "value": 11},
            {"name": "gold necklace", "weight": 1, "value": 2500},
        ],
        "weight": 5,
        "value": 2807,
    }

    assert knapsack(14, items) == {
        "capacity": 14,
        "items": [
            {"name": "tablet", "weight": 7, "value": 1400},
            {"name": "smartphone", "weight": 1, "value": 200},
            {"name": "gold necklace", "weight": 1, "value": 2500},
            {"name": "toaster oven", "weight": 5, "value": 129},
        ],
        "weight": 14,
        "value": 4229,
    }

    items2 = [
        {"name": "desk lamp", "weight": 2, "value": 12},
        {"name": "textbook", "weight": 3, "value": 20},
        {"name": "wall clock", "weight": 2, "value": 15},
        {"name": "frozen dinners", "weight": 10, "value": 50},
        {"name": "tablet", "weight": 7, "value": 1400},
        {"name": "smartphone", "weight": 1, "value": 200},
        {"name": "paper", "weight": 2, "value": 5},
        {"name": "laser printer", "weight": 25, "value": 400},
        {"name": "shoes", "weight": 1, "value": 79},
        {"name": "medicine", "weight": 1, "value": 17},
        {"name": "toaster oven", "weight": 5, "value": 129},
    ]
    assert knapsack(31, items2) == {
        "capacity": 31,
        "items": [
            {"name": "textbook", "weight": 3, "value": 20},
            {"name": "wall clock", "weight": 2, "value": 15},
            {"name": "frozen dinners", "weight": 10, "value": 50},
            {"name": "tablet", "weight": 7, "value": 1400},
            {"name": "smartphone", "weight": 1, "value": 200},
            {"name": "shoes", "weight": 1, "value": 79},
            {"name": "medicine", "weight": 1, "value": 17},
            {"name": "toaster oven", "weight": 5, "value": 129},
        ],
        "weight": 30,
        "value": 1910,
    }
    assert knapsack(36, items2) == {
        "capacity": 36,
        "items": [
            {"name": "tablet", "weight": 7, "value": 1400},
            {"name": "smartphone", "weight": 1, "value": 200},
            {"name": "laser printer", "weight": 25, "value": 400},
            {"name": "shoes", "weight": 1, "value": 79},
            {"name": "medicine", "weight": 1, "value": 17},
        ],
        "weight": 35,
        "value": 2096,
    }
    assert knapsack(100, items2) == {
        "capacity": 100,
        "items": [
            {"name": "desk lamp", "weight": 2, "value": 12},
            {"name": "textbook", "weight": 3, "value": 20},
            {"name": "wall clock", "weight": 2, "value": 15},
            {"name": "frozen dinners", "weight": 10, "value": 50},
            {"name": "tablet", "weight": 7, "value": 1400},
            {"name": "smartphone", "weight": 1, "value": 200},
            {"name": "paper", "weight": 2, "value": 5},
            {"name": "laser printer", "weight": 25, "value": 400},
            {"name": "shoes", "weight": 1, "value": 79},
            {"name": "medicine", "weight": 1, "value": 17},
            {"name": "toaster oven", "weight": 5, "value": 129},
        ],
        "weight": 59,
        "value": 2327,
    }


def main_iter():
    test_knapsack(knapsack=iter_knapsack)

def main_recur():
    test_knapsack(knapsack=recur_knapsack)

def main_back():
    test_knapsack(knapsack=back_knapsack)



if __name__ == '__main__':
    duration = timeit.timeit(main_recur, number=100)
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] Recursive finished in {duration:.2f} seconds.")

    duration = timeit.timeit(main_iter, number=100)
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] Iterative finished in {duration:.2f} seconds.")

    duration = timeit.timeit(main_back, number=100)
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] Backtracking finished in {duration:.2f} seconds.")
