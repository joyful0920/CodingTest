from copy import deepcopy
import sys
si = sys.stdin.readline

r, c = map(int, si().split())
graph = [list(map(str, si().rstrip())) for _ in range(r)]
temp = deepcopy(graph)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for x in range(r):
    for y in range(c):
        if temp[x][y] == 'X':
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (0 <= nx < r and 0 <= ny < c and temp[nx][ny] == '.') or ((0 > nx or nx >= r) or (0 > ny or ny >= c)):
                    cnt += 1
                    if cnt == 3:
                        graph[x][y] = '.'
                        break
                    
island_x = []
island_y = []
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'X':
            island_x.append(i)
            island_y.append(j)

for i in range(min(island_x), max(island_x) + 1):
    for j in range(min(island_y), max(island_y) + 1):
        print(graph[i][j], end='')
    print()