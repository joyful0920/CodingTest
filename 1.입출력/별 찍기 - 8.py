import sys
si = sys.stdin.readline

n = int(si())

for i in range(1, n + 1):
    print('*' * i + ' ' * (2 * n - 2 * i) + '*' * i)

for i in range(1, n):
    print('*' * (n - i) + ' ' * (2 * i) + '*' * (n - i))