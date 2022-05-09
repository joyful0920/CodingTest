import heapq
import sys
si = sys.stdin.readline
INF = float('inf')

n = int(si())
m = int(si())

graph = [[] for _ in range(n + 1)] # 간선 정보를 담을 2차원 배열
distance = [INF] * (n + 1) # 최단 거리 테이블은 무한으로 초기화

for _ in range(m): # 노드 간의 간선 정보 저장
    a, b, cost = map(int, si().split())
    graph[a].append((b, cost)) # a ~ b의 비용 = cost

start, end = map(int, si().split())

# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하고, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0 # 시작 노드의 최단 거리는 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드들 확인
        for node_index, node_cost in graph[now]:
            cost = dist + node_cost # 현재 노드를 거쳐 인접 노드로 가는 비용 = 현재 노드까지의 최소 비용 + 현재 노드 ~ 인접 노드 비용
            if cost < distance[node_index]: # 해당 비용이 기존에 저장되어 있는 최소 비용보다 작을 경우
                distance[node_index] = cost # 새롭게 해당 노드까지의 거리(비용) 갱신
                heapq.heappush(q, (cost, node_index)) # 최단거리가 갱신될 때만 해당 노드를 우선순위큐에 삽입

dijkstra(start)
print(distance[end])