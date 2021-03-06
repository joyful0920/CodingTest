import heapq, sys
si = sys.stdin.readline
INF = int(1e9) # 무한의 의미로 10억 설정

# 도시 개수 n, 통로 개수 m, 메세지 송신 도시 c 입력
n, m, c = map(int, si().split())

# 도시 간 연결된 통로 정보를 담을 2차원 리스트
graph = [[] for _ in range(n + 1)]
# 메세지 전송 소요 시간을 담을 테이블
time = [INF] * (n + 1)

# 도시 간 연결된 통로에 대한 정보 입력
for _ in range(m):
    x, y, z = map(int, si().split())
    graph[x].append((y, z)) # x에서 y까지의 전송 소요시간은 z

# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    # c 도시 자기 자신으로의 전송 소요 시간은 0으로 설정하고 큐에 삽입
    heapq.heappush(q, (0, start))
    time[start] = 0
    while q:
        # 전송 소요 시간이 가장 적게 걸리는 통로 정보 꺼내기
        trans, now = heapq.heappop(q)
        # 현재 도시가 최소 전송 소요 시간 처리된 도시라면 무시
        if time[now] < trans:
            continue
        # 현재 도시와 연결된 다른 인접 도시 확인
        for i in graph[now]:
            cost = trans + i[1] # trans + graph[i][1]
            #인접 도시까지의 전송 시간이 현재 도시를 거쳐갈 때가 더 짧은 경우
            if cost < time[i[0]]: # time(graph[i][0])
                time[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) # (cost, graph[i][0])-

# 다익스트라 알고리즘 수행
dijkstra(c)

# 메세지를 받는 도시의 총 개수와 소요 시간 출력
cnt = 0
max_time = 0
for i in range(1, n + 1):
    if time[i] != INF:
        cnt += 1
        max_time = max(max_time, time[i])
print(cnt - 1, max_time) # 자기 자신으로의 카운트는 빼고 출력