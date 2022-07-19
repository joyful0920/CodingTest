import sys

si = sys.stdin.readline


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


n = int(si())

cnt = 0
for i in str(factorial(n))[::-1]:
    if i != '0':
        break
    cnt += 1

print(cnt)
