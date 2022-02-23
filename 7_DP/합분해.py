import sys
si = sys.stdin.readline

# n, k 입력
n, k = map(int, si().split())

# DP 테이블
d = [[0] * 201 for i in range(201)]

for i in range(201):
    d[1][i] = 1
    d[2][i] = i + 1
    
for i in range(2, 201):
    d[i][1] = i
    for j in range(2, 201):
        d[i][j] = (d[i][j - 1] + d[i - 1][j]) % 1000000000

print(d[k][n])