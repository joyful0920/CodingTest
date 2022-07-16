import sys
from collections import deque
si = sys.stdin.readline

n, l, r = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, index):
    united = []
    united.append((x, y))
    queue = deque()
    queue.append((x, y))
    union[x][y] = index
    total = graph[x][y]
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    queue.append((nx, ny))
                    union[nx][ny] = index
                    total += graph[nx][ny]
                    cnt += 1
                    united.append((nx, ny))
    for i, j in united:
        graph[i][j] = total // cnt
    
result = 0
while True:
    index = 0
    union = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                bfs(i, j, index)
                index += 1
    if index == n * n:
        break
    result += 1

print(result)