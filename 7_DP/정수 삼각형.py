import sys
si = sys.stdin.readline

n = int(si())
triangle = [list(map(int, si().split())) for _ in range(n)]

d = [[0] * n for _ in range(n)]
d[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(i + 1):
        for k in range(-1, 1):
            if 0 <= j + k < n:
                d[i][j] = max(d[i][j], d[i - 1][j + k] + triangle[i][j])

print(max(map(max, d)))