from re import S
import sys
si = sys.stdin.readline

n = int(si())
command = si().rstrip()

# 방향 전환 인덱스
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
now = 0 # 현재는 남쪽 방향

# 미로 탐색
x = 0
y = 0
loads = [(0, 0)] # (0, 0)부터
for c in command:
    if c == 'R':
        now = (now + 1) % 4
    elif c == 'L': # 반례 처리 : 방향 인덱스가 -가 될 경우
        now = (now - 1) if now != 0 else 3
    else:
        x += dx[now]
        y += dy[now]
        loads.append((x, y))

# 미로의 가로, 세로 사이즈 구하기
sorted_x = sorted(loads, key=lambda x:x[0])
sorted_y = sorted(loads, key=lambda x:x[1])
min_x, max_x = sorted_x[0][0], sorted_x[-1][0]
min_y, max_y = sorted_y[0][1], sorted_y[-1][1]

maze = [['#'] * (max_y - min_y + 1) for _ in range(max_x - min_x + 1)]

# 반례 처리 : 미로 탐색할 때 기록한 위치가 음수일 경우
for i in range(len(loads)):
    loads[i] = (loads[i][0] - min_x, loads[i][1] - min_y)


for i, j in loads:
    maze[i][j] = '.'

for x in maze:
    print(''.join(x))