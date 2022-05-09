import sys
si = sys.stdin.readline
INF = float('inf')

n, m = map(int, si().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, si().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        # 둘 중 하나가 INF가 아니라면 두 사람 키 비교가 가능함을 의미
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt += 1
    if cnt == n: # 현재 학생 i는 다른 모든 학생과의 키 비교가 가능함을 의미
        result += 1

print(result)