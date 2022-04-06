import sys
from itertools import combinations
si = sys.stdin.readline

n, m, k = map(int, si().split())

result = 0
all = list(combinations([i for i in range(n)], m))
for i in all:
    cnt = 0
    for j in range(m):
        if i[j] < m:
            cnt += 1
    if cnt >= k:
        result += 1

print(result / len(all))