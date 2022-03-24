import sys
si = sys.stdin.readline

# 카드개수 n 입력
n = int(si())

# 카드 가격 입력
card_price = [0] + list(map(int, si().split()))

# DP 테이블
d = [0] * (n + 1)
d[1] = card_price[1] # 필요한 카드가 1장인 경우

for i in range(2, n + 1):
    for j in range(1, i + 1):
        d[i] = max(d[i], d[i - j] + card_price[j])

print(d[n])