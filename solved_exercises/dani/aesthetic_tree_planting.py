""" A gardener consider aesthetically appealing gardens in which
the tops of sequential physical trees (eg palm trees) are always
sequentially going up and down, that is:
|               |
|       |       |
|   |   |   |   |
Invalid variants:
|               
|  |
|  |  |         

|  |
|  |
|  |
Given a sequence of physical trees in a garden, what is 
the minimum number of physical trees which must be cropped/cut in order
to achieve the pattern desired by that gardener?
"""
def intercalate_lists(a, b):
    c = list(zip(a, b))
    return [elt for sublist in c for elt in sublist]

def aesthetic_tree_planting(random_trees):
    sorted_trees = sorted(random_trees, reverse=True)
    high_trees = sorted_trees[:len(sorted_trees)//2]
    low_trees = sorted_trees[len(sorted_trees)//2:]
    
    print(high_trees, low_trees)
    planting_trees = intercalate_lists(high_trees, low_trees)
    if len(high_trees) != len(low_trees):
        planting_trees.insert(0, sorted_trees[-1])
    

    return planting_trees


def print_trees_sequence(trees_sequence):
    print("|   " * len(trees_sequence) + "\n", end="")
    for i in range(1, max(trees_sequence)):
        for tree in trees_sequence:
            if tree - i > 0:
                print("|   ", end="")
            else:
                print("    ", end="")
        print("")


def main():
    """local testing of aesthetic_tree_planting"""
    random_trees = [1, 5, 1 ,2, 5, 4, 3, 3]
    expected = [5, 3, 5, 2, 4, 1, 3, 1]
    result = aesthetic_tree_planting(random_trees)
    print_trees_sequence(result)
    print(f" >> input {random_trees} expected is {expected}, actual is {result}")
    print(f"Result is {expected == result}")

    random_trees = [1, 5, 1 ,2, 5, 4, 3]
    expected = [1, 5, 3, 5, 2, 4, 1]
    result = aesthetic_tree_planting(random_trees)
    print_trees_sequence(result)
    print(f" >> input {random_trees} expected is {expected}, actual is {result}")
    print(f"Result is {expected == result}")

    random_trees = [3, 3, 3, 3]
    expected = [3, 3, 3, 3]
    result = aesthetic_tree_planting(random_trees)
    print_trees_sequence(result)
    print(f" >> input {random_trees} expected is {expected}, actual is {result}")
    print(f"Result is {expected == result}")
    
if __name__ == "__main__":
    main()
