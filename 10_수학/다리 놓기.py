import sys
si = sys.stdin.readline

t = int(si())

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

for _ in range(t):
    n, m = map(int, si().split())
    # 이항계수(n개의 수 중 순서없이 k개를 뽑는 조합의 가짓수) 개념 사용
    result = factorial(m) // (factorial(n) * factorial(m - n))
    print(result)