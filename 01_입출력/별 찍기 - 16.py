import sys
si = sys.stdin.readline

n = int(si())

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' + ' *' * (i - 1))