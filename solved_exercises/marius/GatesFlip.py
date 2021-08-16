"""
Prison guard problem
You have N prison guards and M cell gates. The status of the gates can be open (1) or closed (0).
At the beginning, all the cell gates are closed.
Every prison guard go through the cell gates opens the closed gates and closes the opened gates the following way:
first prison guard goes through all the gates and opens all of them
second prison guard goes through every second cell gate and closes the open ones
third prison guard goes through every third cell gate and opens the closed ones, and closes the opened ones etc.
Your task is to write an application which gets the N (guard number) and M (gate number) as a parameter and
returns an int[] with the status of the cell gates after all the guards went through the gates.
Sample input:
N = 5, M = 5
Sample output:
1, 0, 0, 1, 0
"""
def flip_gates(guardians, gates):
    flipped_gates = list(gates)
    for i in range(guardians):
        step = i + 1
        for elem in range(i, len(gates), step):
            flipped_gates[elem] = (flipped_gates[elem] + 1) % 2
    return flipped_gates


def main():
    gates = [0, 0, 0, 0, 0]
    print(flip_gates(5, gates))


if __name__ == '__main__':
    main()
