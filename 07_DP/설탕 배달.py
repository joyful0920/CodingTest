import sys
si = sys.stdin.readline
INF = float('inf')

n = int(si())

d = [INF] * 5001
d[3] = 1
d[5] = 1
d[6] = 2

for i in range(8, n + 1):
    if (d[i - 5] != INF) and (d[i - 3] != INF):
        d[i] = min(d[i - 5] + 1, d[i - 3] + 1)
    elif d[i - 5] != INF:
        d[i] = d[i - 5] + 1
    elif d[i - 3] != INF:
        d[i] = d[i - 3] + 1

if d[n] == INF:
    print(-1)
else:
    print(d[n])