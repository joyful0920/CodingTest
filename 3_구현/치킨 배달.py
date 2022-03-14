
import sys
from itertools import combinations
si = sys.stdin.readline
INF = float('inf')

n, m = map(int, si().split())
house, chicken = [], []

for r in range(n):
    array = list(map(int, si().split()))
    for c in range(n):
        if array[c] == 1:
            house.append((r, c))
        elif array[c] == 2:
            chicken.append((r,c))

# m개의 치킨집을 뽑는 모든 조합 계산
choose = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def chick_len(choose):
    result = 0
    for hx, hy in house:
        length = INF
        for cx, cy in choose:
            length = min(length, abs(hx - cx) + abs(hy - cy))
        result += length
    return result

result = INF
for i in choose:
    result = min(result, chick_len(i))

print(result)
