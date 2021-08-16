def recursive_knapsak(capacity, items):
    max_packed_weight = 0
    if len(items) == 0:
        print("am iesit pe aici")
        return max_packed_weight

    for i, item_weight in enumerate(items):
        if item_weight > capacity:
            continue
        print("item evaluat",item_weight, "de pe pozitia", i)
        remaining_capacity = capacity - item_weight
        remaining_items = items[i + 1 :]
        print("remaining_capacity is ", remaining_capacity, "remaining items",remaining_items)
        print("---------entry-----------")
        weight = recursive_knapsak(remaining_capacity, remaining_items)
        
        print("in afara if",max_packed_weight)
        if item_weight + weight  > max_packed_weight:
            max_packed_weight = weight + item_weight
            print("in if dupa add",max_packed_weight)
    print("------------exit-----------")
    return max_packed_weight


def knapsack(capacity, items):
    return {
        "capacity": capacity,
        "weight": recursive_knapsak(capacity, items),
    }


def test_knapsack():
    items = [2, 3, 10, 7]
    # assert knapsack(0, items) == {"capacity": 0, "weight": 0}
    # assert knapsack(1, items) == {
    #     "capacity": 1,
    #     "weight": 0,
    # }
    # assert knapsack(2, items) == {
    #     "capacity": 2,
    #     "weight": 2,
    # }
    # assert knapsack(5, items) == {
    #     "capacity": 5,
    #     "weight": 5,
    # }
    print("********************")
    # assert knapsack(14, items) == {
    #     "capacity": 14,
    #     "weight": 13,
    # }
    # assert knapsack(18, items) == {
    #     "capacity": 18,
    #     "weight": 17,
    # }
    items2 = [2, 4, 1]
    assert knapsack(5, items2) == {"capacity": 6, "weight": 5}