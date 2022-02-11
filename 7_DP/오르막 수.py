import sys
si = sys.stdin.readline

n = int(si())

d = [[0] * 10 for _ in range(n + 1)]

# 1 자리수는 1로 초기화
for i in range(10):
    d[1][i] = 1

# 보톰업 DP
for i in range(2, n + 1):
    for j in range(10):
        for k in range(j, 10):
            d[i][j] += d[i - 1][k]

print(sum(d[n]) % 10007)