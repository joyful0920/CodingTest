import sys
si = sys.stdin.readline

n, k = map(int, si().split())

rank = []
for _ in range(n):
    c, g, s, b = map(int, si().split())
    rank.append((c, g, s, b))
    if c == k:
        target = (c, g, s, b)

rank.sort(key=lambda x : (-x[1], -x[2], -x[3], x[0]))

cnt = 0
for i in range(n):
    if rank[i][0] != k and rank[i][1] == target[1] and rank[i][2] == target[2] and rank[i][3] == target[3]:
        cnt += 1
    if rank[i][0] == k:
        print(i + 1 - cnt)
        break