import sys
si = sys.stdin.readline

# 잔 개수 입력
n = int(si())
# 포도주 양 입력
w = [0] * 10001
for i in range(1, n + 1):
    w[i] = int(si())

# 마실 수 있는 포도주양 DP 테이블
d = [0] * 10001
d[1] = w[1]

# 보톰업 DP
if n > 1:
    d[2] = w[1] + w[2]
    for i in range(3, n + 1):
        d[i] = max(d[i - 1], d[i - 3] + w[i - 1] + w[i], d[i - 2] + w[i])

print(d[n])