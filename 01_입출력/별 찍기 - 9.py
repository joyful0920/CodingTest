import sys
si = sys.stdin.readline

n = int(si())

for i in range(0, n):
    print(' ' * i + '*' * (2 * n - (2 * (i + 1) - 1)))

for i in range(1, n):
    print(' ' * (n - 1 - i) + '*' * (2 * i + 1))