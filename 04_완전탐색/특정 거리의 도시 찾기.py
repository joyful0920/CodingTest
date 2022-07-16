import sys
from collections import deque
si = sys.stdin.readline
INF = float('inf')

n, m, k, x = map(int, si().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, si().split())
    graph[a].append(b)

distance = [INF for _ in range(n + 1)]
distance[x] = 0
queue = deque()
queue.append(x)

def bfs():
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if distance[next] == INF:
                distance[next] = distance[now] + 1
                queue.append(next)

bfs()

result = deque()
for i in range(1, n + 1):
    if distance[i] == k:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i)