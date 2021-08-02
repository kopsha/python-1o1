# tail recursion
#  F(0) = 0,
#  F(1) = 1,
#  F(n) =  F(n-1) + F(n-2)
#  F(n) =  F(n-2) + F(n-1)

from functools import lru_cache

# memoization
@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)


def fibonacci_sequence_v1(n):
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]

    sequence = list((0, 1,))
    for _ in range(n-2):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence


def fibonacci_v2(n, memory={}):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memory:
        return memory[n]
    value = fibonacci_v2(n-2) + fibonacci_v2(n-1)
    memory[n] = value
    return value


def fibonacci_sequence_v2(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def fibonacci_sequence_inf():
    x = 0
    y = 1
    while True:
        yield x
        x, y = y, x + y


def main():
    N = 10
    print(f"The first {N} fibonacci numbers:")

    first_twenty_generator = fibonacci_sequence_v2(20)

    for x in first_twenty_generator:
        print(x)

    generator = fibonacci_sequence_inf()
    for i in range(20):
        print(next(generator))

if __name__ == '__main__':
    main()
