from copy import deepcopy
import sys
sys.setrecursionlimit(10**9)
si = sys.stdin.readline

# 수족관 그래프
graph = [[None] * 4 for _ in range(4)]

# 각 칸에 물고기 정보([번호, 방향]) 입력
for i in range(4):
    data = list(map(int, si().split()))
    for j in range(4):
        graph[i][j] = [data[j * 2], data[j * 2 + 1] - 1]

# 방향 인덱스 (반시계 방향)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 물고기 이동 및 회전 함수
def find(graph, index):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == index:
                return (i, j)
    return None

def fish(graph, shark_x, shark_y):
    for i in range(1, 17):
        # 물고기 위치 찾기
        position = find(graph, i)
        if position != None:
            x, y = position[0], position[1]
            di = graph[x][y][1]
            # 해당 물고기의 방향으로 이동 가능한지 확인
            for _ in range(8):
                nx = x + dx[di]
                ny = y + dy[di]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx == shark_x and ny == shark_y):
                        graph[x][y][1] = di
                        graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
                        break
                # 불가하면 회전
                di = (di + 1) % 8

# 상어가 먹을 수 있는 물고기 위치 반환 함수
def shark(graph, shark_x, shark_y):
    di = graph[shark_x][shark_y][1]
    fishes = []
    for _ in range(4):
        shark_x += dx[di]
        shark_y += dx[di]
        if 0 <= shark_x < 4 and 0 <= shark_y < 4:
            if graph[shark_x][shark_y][0] != -1:
                fishes.append((shark_x, shark_y))
    return fishes

result = 0
# DFS
def dfs(graph, shark_x, shark_y, total):
    global result
    graph = deepcopy(graph)

    # 상어가 위치한 곳의 물고기 먹기
    total += graph[shark_x][shark_y][0]
    graph[shark_x][shark_y][0] = -1

    # 전체 물고기 이동
    fish(graph, shark_x, shark_y)

    # 상어 먹을 수 있는 물고기 위치 찾기
    fishes = shark(graph, shark_x, shark_y)
    # 먹을 수 있는 물고기가 없다면
    if len(fishes) == 0:
        result = max(result, total)
        return
    # 먹을 수 있는 물고기들에 대해 모두 dfs 실행
    for shark_nx, shark_ny in fishes:
        dfs(graph, shark_nx, shark_ny, total)
    
dfs(graph, 0, 0, 0)
print(result)