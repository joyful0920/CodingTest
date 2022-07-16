import heapq, sys
si = sys.stdin.readline
INF = float('inf')

n, m = map(int ,si().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    a, b, c = map(int, si().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        cur_cost, now = heapq.heappop(q)
        if distance[now] < cur_cost:
            continue
        for next_node, next_cost in graph[now]:
            temp = cur_cost + next_cost
            if distance[next_node] > temp:
                distance[next_node] = temp
                heapq.heappush(q, (temp, next_node))

dijkstra(2)

d = [0] * (n + 1)
d[2] = 1

def route(cur_node):
    if d[cur_node] == 0:
        for next_node, next_cost in graph[cur_node]:
            if distance[cur_node] > distance[next_node]:
                d[cur_node] += route(next_node)
        return d[cur_node]
    else:
        return d[cur_node]

print(route(1))