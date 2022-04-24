import sys
from collections import deque
si = sys.stdin.readline

n, m = map(int, si().split())
graph = [list(map(int, si().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        a, b, c = queue.popleft()
        if a == n - 1 and b == m - 1:
            return visited[a][b][c]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and z == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1 
                    queue.append((nx, ny, 1))
                elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][1] = visited[x][y][z] + 1
                    queue.append((nx, ny, z))
    return -1
    return -1


print(bfs(0, 0, 0))