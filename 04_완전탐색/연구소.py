from itertools import combinations
from collections import deque
from copy import deepcopy
import sys
si = sys.stdin.readline

# N, M, 지도 입력
n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]

# 벽을 세울 수 있는 좌표 튜플을 리스트에 저장
wall = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            wall.append((i, j))

# 확인할 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스가 퍼지는 걸 수행할 BFS 함수
def bfs():
    # 바이러스의 좌표를 queue에 저장
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 지도 범위 내이고, 바이러스가 퍼질 수 있는 경우에만
            if 0 <= nx < n and 0 <= ny < m and graph_copy[nx][ny] == 0:
                graph_copy[nx][ny] = 2
                queue.append((nx, ny))
        
result = [] # 안전구역 크기 결과를 저장할 리스트
# 벽을 세울 세 곳의 조합을 모두 구한 후 각각 반복
for picked in list(combinations(wall, 3)):
    # 일단 graph의 카피본을 떠놓고
    graph_copy = deepcopy(graph)
    # 뽑은 세 곳에 벽 세우기
    for each_picked in picked:
        x, y = each_picked
        graph_copy[x][y] = 1
    # 그리고 BFS 수행
    bfs()
    # 안전구역 크기 계산
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph_copy[i][j] == 0:
                cnt += 1
    result.append(cnt)

print(max(result))