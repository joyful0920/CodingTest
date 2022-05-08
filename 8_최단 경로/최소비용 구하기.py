import heapq
import sys
si = sys.stdin.readline
INF = float('inf')

n = int(si())
m = int(si())

# 2차원 리스트 생성 및 비용 무한으로 초기화
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

# 노드와 간선 간의 정보 입력
for _ in range(m):
    x, y, z = map(int, si().split())
    graph[x].append((y, z))

start, end = map(int, si().split())

# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 기존에 저장된 현재 노드까지의 거리가 현재 루트의 거리보다 작은 경운 무시
            continue
        for i in graph[now]:
            cost = dist + i[1] # 현재 노드와 연결되어 있는 다른 노드까지의 거리를 추가하여
            if cost < distance[i[0]]: # 해당 비용이 기존에 저장되어 있는 비용보다 작을 경우
                distance[i[0]] = cost # 새롭게 해당 노드까지의 거리(비용) 갱신
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

print(distance[end])