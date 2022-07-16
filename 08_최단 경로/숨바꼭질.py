import heapq
import sys
si = sys.stdin.readline
INF = float('inf')

n, m = map(int, si().split())

graph = [[] for _ in range(n)]
distance = [INF] * n

for _ in range(m):
    a, b = map(int, si().split())
    graph[a - 1].append((b - 1, 1))
    graph[b - 1].append((a - 1, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node_index, node_cost in graph[now]:
            cost = dist + node_cost
            if cost < distance[node_index]:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))

dijkstra(0)

num = -1
cnt = 0
for i in range(n):
    if distance[i] == max(distance):
        if num == -1:
            num = i + 1
        cnt += 1

print(num, max(distance,), cnt)