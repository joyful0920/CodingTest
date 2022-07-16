from collections import deque
import sys
si = sys.stdin.readline
INF = float('inf')

n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 상어의 크기와 위치를 나타낼 변수
shark_size = 2
shark_x, shark_y = 0, 0

# 초기 상어 위치를 찾아 상태 업뎃
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            shark_x, shark_y = i, j

# 도착 가능한 위치들의 거리를 계산해 줄 BFS 함수
def bfs():
    visited = [[-1] * n for _ in range(n)]
    visited[shark_x][shark_y] = 0
    q = deque()
    q.append((shark_x, shark_y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 그래프 범위 내이면서 상어가 지나갈 수 있을 경우에만
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and graph[nx][ny] <= shark_size:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return visited

# 먹을 수 있는 물고기 중 가장 가까운 물고기의 위치와 거리를 반환해 줄 함수
def fish(visited):
    fish_x, fish_y = 0, 0
    fish_dist = INF
    for i in range(n):
        for j in range(n):
            # 도착할 수 있는 위치이고, 먹을 수 있는 물고기 중 현재 fish_dist보다 더 가까운 경우만
            if visited[i][j] != -1 and 1 <= graph[i][j] < shark_size and visited[i][j] < fish_dist:
                fish_x, fish_y = i, j
                fish_dist = visited[i][j]
    # 먹을 수 있는 물고기가 없는 경우
    if fish_dist == INF:
        return None
    else:
        return fish_x, fish_y, fish_dist

time = 0
cnt = 0
while True:
    result = fish(bfs())
    # 엄마 상어 호출이 필요한 경우
    if result == None:
        print(time)
        break
    else:
        shark_x, shark_y = result[0], result[1] # fish_x, fish_y
        time += result[2] # += fish_dist
        graph[shark_x][shark_y] = 0
        cnt += 1
        # 먹은 횟수가 상어 사이즈 만큼 도달했을 경우
        if cnt == shark_size:
            shark_size += 1
            cnt = 0