import sys
from copy import deepcopy
si = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]

def dfs(x, y, rain, graph):
    if 0 <= x < n and 0 <= y < n and graph[x][y] - rain > 0:
        graph[x][y] = 0
        dfs(x - 1, y, rain, graph)
        dfs(x + 1, y, rain, graph)
        dfs(x, y - 1, rain, graph)
        dfs(x, y + 1, rain, graph)
        return True

max_area = 0
for rain in range(100):
    graph_copy = deepcopy(graph)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if dfs(i, j, rain, graph_copy) == True:
                cnt += 1
    max_area = max(max_area, cnt)

print(max_area)