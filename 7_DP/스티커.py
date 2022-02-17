import sys
si = sys.stdin.readline

t = int(si())

for _ in range(t):
    n = int(si())
    d = [list(map(int, si().split())) for _ in range(2)]
    if n == 1:
        print(max(d[0][0], d[1][0]))
    elif n == 2:
        print(max(d[0][0] + d[1][1], d[1][0] + d[0][1]))
    else:
        d[0][1] += d[1][0]
        d[1][1] += d[0][0]
        for i in range(2, n):
            d[0][i] += max(d[1][i - 1], d[1][i - 2])
            d[1][i] += max(d[0][i - 1], d[0][i - 2])
        print(max(d[0][n - 1], d[1][n - 1]))