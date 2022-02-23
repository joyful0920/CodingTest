import sys
si = sys.stdin.readline

# 카드개수 n 입력
n = int(si())

# 카드 가격 입력
array = [0] + list(map(int, si().split()))

# DP 테이블
d = [0] * (n + 1)
d[1] = array[1]

for i in range(2, n + 1):
    for j in range(1, i + 1):
        d[i] = max(d[i], d[i - j] + array[j])

print(d[n])