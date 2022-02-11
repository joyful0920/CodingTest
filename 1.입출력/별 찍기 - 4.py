import sys
si = sys.stdin.readline

n = int(si())

for i in range(0, n):
    print(' ' * i + '*' * (n - i))