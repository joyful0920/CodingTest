import sys
si = sys.stdin.readline

INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

# 회사의 개수 n과 경로의 개수 m 입력
n, m = map(int, si().split())

# 2차원 리스트를 생성 및 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 같은 회사로의 이동 시간은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] == 0

# 연결된 회사 번호 정보 입력
for _ in range(m):
    a, b = map(int, si().split())
    graph[a][b] = 1 # 다른 회사로의 이동시간은 모두 1로 초기화
    graph[b][a] = 1 # 반대 방향도 동일

# 종점 회사 x와 거점 회사 x 입력
x, k = map(int, si().split())
start = 1 # 출발 지점은 1

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][b] + graph[k][b])

# 1번에서 출발하여 k를 거쳐 x로 가는 최단 시간 경로 출력
distance = graph[start][k] + graph[k][x]
if distance >= INF:
    print(-1)
else:
    print(distance)