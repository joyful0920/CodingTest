import heapq
import sys
si = sys.stdin.readline
INF = float('inf')

n, m, x = map(int, si().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, cost = map(int, si().split())
    graph[a].append((b, cost))

def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node_index, node_cost in graph[now]:
            cost = dist + node_cost
            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))

    return distance

result = 0
for i in range(1, n + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x] + back[i])

print(result)