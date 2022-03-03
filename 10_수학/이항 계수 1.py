import sys
si = sys.stdin.readline

n, k = map(int, si().split())

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

result = factorial(n) // (factorial(k) * factorial(n - k))

print(result)