import sys
from collections import deque
si = sys.stdin.readline

# 가로 M, 세로 N 입력
m, n = map(int, si().split())

# 토마토 상자 정보 입력
graph = [list(map(int, si().split())) for _ in range(n)]
day = 0 # 날짜 초기화

# 확인할 방향 정의(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 처음 토마토의 좌표를 queue에 삽입(익은 토마토만)
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

# BFS 함수 (너비 우선 탐색)
def bfs():
    while queue:
        x, y = queue.popleft()
        # 현재 칸에서 상화좌우로 옆칸 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 상자 범위 내이고 안익은 토마토가 있는 경우에만
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                # 직전 좌표의 요소 값에 +1 해준 값으로 해당 좌표의 토마토가 익기까지 걸린 날짜를 저장
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny)) # 해당 좌표를 큐에 삽입

bfs()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
        else:
            day = max(day, graph[i][j])

# 시작할 때 익은 토마토의 값이 1이었기 때문에 최종 계산값에 1을 빼주기
print(day - 1)