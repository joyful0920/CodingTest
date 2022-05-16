import sys
si = sys.stdin.readline

graph = [list(map(int, si().split())) for _ in range(19)]

dx = [1, 1, 0, -1] # 하(↓), 우하(⬊), 우(➞), 우상(⬈)
dy = [0, 1, 1, 1]

for x in range(19):
    for y in range(19):
        if graph[x][y] == 1 or graph[x][y] == 2:
            color = graph[x][y]
            for i in range(4):
                cnt = 1
                nx = x + dx[i]
                ny = y + dy[i]
                while 0 <= nx < 19 and 0 <= ny < 19 and graph[nx][ny] == color:
                    cnt += 1
                    if cnt == 5:
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and graph[nx + dx[i]][ny + dy[i]] == color:
                            break
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and graph[x - dx[i]][y - dy[i]] == color:
                            break
                        print(color)
                        print(x + 1, y + 1)
                        exit(0)
                    nx += dx[i]
                    ny += dy[i]

print(0)