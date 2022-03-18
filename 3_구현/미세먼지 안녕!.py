import sys
si = sys.stdin.readline

r, c, t = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(r)]

# 공기청정기 위치 구하기
for i in range(r):
    if graph[i][0] == -1:
        up = i
        down = i + 1
        break

# 미세먼지 확산 함수
def pm():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    temp = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if graph[i][j] != 0 and graph[i][j] != -1:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                        temp[nx][ny] += graph[i][j] // 5
                        cnt += 1
                graph[i][j] -= (graph[i][j] // 5 * cnt)
    
    for i in range(r):
        for j in range(c):
            graph[i][j] += temp[i][j]

# 공기청정기 위쪽 방향의 흐름
def cleaner_up():
    # 반시계 방향
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        # 이렇게 한줄로 표현하면 temp 없이 두값 교환 가능
        graph[x][y], before = before, graph[x][y]
        x = nx
        y = ny

# 공기청정기 아래쪽 방향의 흐름
def cleaner_down():
    # 시계 방향
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = nx
        y = ny

for _ in range(t):
    pm()
    cleaner_up()
    cleaner_down()

answer = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            answer += graph[i][j]

print(answer)