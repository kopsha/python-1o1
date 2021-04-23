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
knapsack(0, items) ➞ {
  "capacity": 0,
  "items": [],
  "weight": 0,
  "value": 0
}
"""


from abc import abstractproperty


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

def iterative_knapsack(capacity, items):
    n = len(items)
    weights = [item["weight"] for item in items]
    values = [item["value"] for item in items]
    items_value = 0
    items_weight = 0
    knapsack_items = []

    process = [[0 for w in range(capacity+1)] for i in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, capacity+1):
            item_index = i-1
            item_weight = weights[item_index]
            item_value = values[item_index]
            if item_weight <= w:
                case1 = process[i-1][w]
                case2 = item_value + process[i-1][w-item_weight]
                if case1 >= case2:
                    process[i][w] = case1
                    items_value = item_value
                    items_weight = item_weight
                    knapsack_items = [items[i-1]]
                    print("knapsack_items",knapsack_items)
                else:
                    process[i][w] = case2
                    items_value = item_value
                    items_weight = item_weight
                    knapsack_items = [items[i-1]] #+ [item for item in knapsack_items]
                    print("knapsack_items else",knapsack_items)
            else:
                process[i][w] = process[i-1][w]
                
    print(process)

    items_value = process[n][capacity]
    print(items_weight)
    print(items_value)
    print(knapsack_items)
    return items_value, knapsack_items, items_weight

def knapsack(capacity, items):
    knapsack_items = []
    items_weight = 0
    items_value = 0
    # items_value, knapsack_items, items_weight = recursive_knapsak(capacity, items)
    items_value, knapsack_items, items_weight = iterative_knapsack(capacity, items)

    return {
        "capacity": capacity,
        "items": knapsack_items,
        "weight": items_weight,
        "value": items_value,
    }

def test_knapsack():
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
    