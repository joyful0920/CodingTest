import sys, copy
sys.setrecursionlimit(10**9)
si = sys.stdin.readline

n = int(si())
graph1 = [list(map(str, si().rstrip())) for _ in range(n)]
graph2 = copy.deepcopy(graph1)

for i in range(n):
    for j in range(n):
        if graph2[i][j] == 'R':
            graph2[i][j] = 'G'

copy1 = copy.deepcopy(graph1)
copy2 = copy.deepcopy(graph2)


def dfs1(x, y, target):
    if 0 <= x < n and 0 <= y < n and copy1[x][y] == target and copy1[x][y] != 0:
        copy1[x][y] = 0
        dfs1(x - 1, y, target)
        dfs1(x + 1, y, target)
        dfs1(x, y - 1, target)
        dfs1(x, y + 1, target)
        return True

def dfs2(x, y, target):
    if 0 <= x < n and 0 <= y < n and copy2[x][y] == target and copy2[x][y] != 0:
        copy2[x][y] = 0
        dfs2(x - 1, y, target)
        dfs2(x + 1, y, target)
        dfs2(x, y - 1, target)
        dfs2(x, y + 1, target)
        return True

cnt1 = 0
cnt2 = 0
for i in range(n):
    for j in range(n):
        if dfs1(i, j, graph1[i][j]) == True:
            cnt1 += 1
        if dfs2(i, j, graph2[i][j]) == True:
            cnt2 += 1

print(cnt1, cnt2)