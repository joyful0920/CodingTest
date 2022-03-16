from itertools import combinations
import sys
si = sys.stdin.readline

n, m = map(int, si().split())
array = [i for i in range(1, n + 1)]
ice = [[False for _ in range(n + 1)] for _ in range(n + 1)]
cnt = 0

for _ in range(m):
    a, b = map(int, si().split())
    ice[a][b] = True
    ice[b][a] = True

ice_comb = list(combinations(array, 3))

for i in ice_comb:
    if ice[i[0]][i[1]] or ice[i[0]][i[2]] or ice[i[1]][i[2]]:
        continue
    cnt += 1

print(cnt)