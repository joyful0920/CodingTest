import sys, heapq
si = sys.stdin.readline

n, m, v = map(int, si().split())
graph = [[] for _ in range(n + 1)]
visited = []

for _ in range(m):
    a, b = map(int, si().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

def dfs(start, graph, visited):
    visited.append(start)
    for i in graph[start]:
        if i not in visited:
            dfs(i, graph, visited)

def bfs(start, graph):
    queue = [start]
    visited = [start]
    while queue:
        now = queue.pop(0)
        for i in graph[now]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
    for i in visited:
        print(i, end = ' ')

dfs(v, graph, visited)
for i in visited:
    print(i, end = ' ')
print()
bfs(v, graph)