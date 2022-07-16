import sys
from collections import deque
si = sys.stdin.readline

n, k = map(int, si().split())

graph = [0] * 100001

def bfs(start, end):
    queue = deque()
    queue.append(start)
    while queue:
        x = queue.popleft()
        if x == end:
            return graph[end]
        for i in range(3):
            if i == 0:
                nx = x - 1
                if 0 <= nx < 100001 and graph[nx] == 0:
                    graph[nx] = graph[x] + 1
                    queue.append(nx)
            elif i == 1:
                nx = x + 1
                if 0 <= nx < 100001 and graph[nx] == 0:
                    graph[nx] = graph[x] + 1
                    queue.append(nx)
            else:
                nx = 2 * x
                if 0 <= nx < 100001 and graph[nx] == 0:
                    graph[nx] = graph[x] + 1
                    queue.append(nx)

print(bfs(n, k))