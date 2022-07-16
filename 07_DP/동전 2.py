import sys
si = sys.stdin.readline
INF = float('inf')
n, k = map(int, si().split())

array = list(int(si().rstrip()) for _ in range(n))

d = [INF] * (k + 1)
d[0] = 0

for i in range(n):
    for j in range(array[i], k + 1):
        d[j] = min(d[j], d[j - array[i]] + 1)
    
if d[k] == INF:
    print(-1)
else:
    print(d[k])