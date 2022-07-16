import heapq
import sys
si = sys.stdin.readline

n, k = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
s, x, y = map(int, si().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            heapq.heappush(q, (0, graph[i][j], i, j))

def bfs():
    time = 0
    while q and time < s:
        t, num, xx, yy = heapq.heappop(q)
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = num
                heapq.heappush(q, (t + 1, num, nx, ny))
        if len(q) != 0:
            if time != q[0][0]:
                time += 1

bfs()

print(graph[x - 1][y - 1])