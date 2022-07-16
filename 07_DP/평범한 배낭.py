import sys
si = sys.stdin.readline

n, k = map(int, si().split())

weights = [0]
values = [0]
for _ in range(n):
    w, v = map(int, si().split())
    weights.append(w)
    values.append(v)

d = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if weights[i] <= j:
            d[i][j] = max(d[i - 1][j - weights[i]] + values[i], d[i - 1][j])
        else:
            d[i][j] = d[i - 1][j]

print(d[n][k])