import sys
si = sys.stdin.readline

n, s, m = map(int, si().split())
v = list(map(int, si().split()))

d = [[False] * (m + 1) for _ in range(n + 1)]
d[0][s] = True

for i in range(n):
    for j in range(m + 1):
        if d[i][j]:
            if j - v[i] >= 0:
                d[i + 1][j - v[i]] = True
            if j + v[i] <= m:
                d[i + 1][j + v[i]] = True

result = -1
for i in range(m + 1):
    if d[n][i]:
        result = i

print(result)