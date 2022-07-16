import sys
from collections import deque
si = sys.stdin.readline

n, m = map(int, si().split())
graph = [['O'] * m for _ in range(n)]
cnt = n * m
queen = deque()
knight = deque()

for i in range(3):
    temp = deque(map(int, si().split()))
    for _ in range(temp.popleft()):
        x = temp.popleft() - 1
        y = temp.popleft() - 1
        graph[x][y] = 'X'
        cnt -= 1
        if i == 0:
            queen.append((x, y))
        elif i == 1:
            knight.append((x, y))

qdx = [-1, -1, -1, 0, 1, 1, 1, 0]
qdy = [-1, 0, 1, 1, 1, 0, -1, -1]

def move_queen(x, y):
    global cnt
    for i in range(8):
        nx = x
        ny = y
        while True:
            nx = nx + qdx[i]
            ny = ny + qdy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 'O':
                    graph[nx][ny] = 'V'
                    cnt -= 1
                elif graph[nx][ny] == 'X':
                    break
            else:
                break

kdx = [-1, 1, -2, -2, -1, 1, 2, 2]
kdy = [-2, -2, -1, 1, 2, 2, -1, 1]

def move_knight(x, y):
    global cnt
    for i in range(8):
        nx = x + kdx[i]
        ny = y + kdy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'O':
            graph[nx][ny] = 'V'
            cnt -= 1

while queen:
    x, y = queen.popleft()
    move_queen(x, y)

while knight:
    x, y = knight.popleft()
    move_knight(x, y)

print(cnt)