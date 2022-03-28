import sys
from collections import deque
si = sys.stdin.readline

n = int(si())
graph = [list(si().rstrip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    visited = [[-1] * n for _ in range(n)]
    visited[0][0] = 0
    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        if (x, y) == (n - 1, n - 1):
            print(visited[n - 1][n - 1])
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if graph[nx][ny] == '1':
                    visited[nx][ny] = visited[x][y]
                    queue.appendleft((nx, ny))
                elif graph[nx][ny] == '0':
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

bfs()