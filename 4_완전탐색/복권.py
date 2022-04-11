import sys
from itertools import combinations
si = sys.stdin.readline

n, m, k = map(int, si().split())

result = 0
# n개의 수 중 m개의 수를 뽑는 모든 조합에 대해 반복
all = list(combinations([i for i in range(n)], m))
for i in all:
    cnt = 0
    # 0 ~ m-1 이 당첨 번호라고 가정
    for j in range(m):
        # 현재 뽑은 조합의 번호가 0 ~ m-1에 속한다면
        if i[j] < m:
            cnt += 1 # 카운트 + 1
    if cnt >= k: # 카운트된 수가 k보다 같거나 크면 복권 당첨이 가능한 경우
        result += 1

# 당첨 확률 = 당첨 가능한 경우의 수 / 모든 조합 가짓 수
print(result / len(all))