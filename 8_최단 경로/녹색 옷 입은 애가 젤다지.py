import heapq
import sys
si = sys.stdin.readline
INF = float('inf')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

t = 0
while True:
    n = int(si())
    if n == 0:
        exit(0)

    graph = [list(map(int, si().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]

    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = graph[0][0]
    
    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    t += 1
    print("Problem " + str(t) + ": " + str(distance[n - 1][n - 1]))