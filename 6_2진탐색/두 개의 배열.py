import sys
si = sys.stdin.readline

t = int(si())

for _ in range(t):
    n, m = int(si().split())
    a = list(map(int, si().split()))
    b = sorted(list(map(int, si().split())))

