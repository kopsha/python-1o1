
def fibonacci(n, memo={}):
    if n in memo: return memo[n]
    if n <= 2: return 1
    memo[n] = fibonacci(n-2, memo) + fibonacci(n-1, memo)
    return memo[n]


def main():
    n = 100
    memo = {}
    print(n, "th fibonacci number is", fibonacci(n, memo))
    print(memo)

if __name__ == '__main__':
    main()
