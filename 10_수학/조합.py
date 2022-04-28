import sys
si = sys.stdin.readline

n, m = map(int, si().split())

# 팩토리얼 재귀 함수
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# 조합(이항 계수) nCm = n! / m! * (n - m)!
result = factorial(n) // (factorial(m) * factorial(n - m))

print(result)