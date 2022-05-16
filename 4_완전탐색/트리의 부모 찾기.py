import sys
sys.setrecursionlimit(10**9)
si = sys.stdin.readline

n = int(si())
graph = [[] for _ in range(n + 1)] # 간선 정보를 담을 2차원 배열

# 부모 테이블 생성 및 초기화
parent = [0] * (n + 1)
parent[1] = 1

# 간선 정보 입력
for _ in range(n - 1):
    a, b = map(int, si().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 함수
def dfs(x):
    for i in graph[x]: # 현재 탐색 중인 노드 x와 연결된 다른 노드들 확인
        if parent[i] == 0: # 해당 노드의 부모 노드값이 아직 입력 전이라면
            parent[i] = x # 현재 노드 x를 부모로 설정
            dfs(i) # DFS 함수를 재귀 호출

dfs(1)

for i in range(2, n + 1):
    print(parent[i])