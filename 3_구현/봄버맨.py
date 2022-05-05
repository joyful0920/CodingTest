import sys
si = sys.stdin.readline

r, c, n = map(int, si().split())
graph = [list(map(str, si().rstrip())) for _ in range(r)]
timer = [[0] * c for _ in range(r)] # 폭탄 시간을 저장할 타이머

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'O':
            timer[i][j] = 2 # 초기 상태는 1초를 지났다 생각하고 타이머는 2로

# 폭발 함수
def explosion(x, y):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    graph[x][y] = '.'
    timer[x][y] = 0
    for i in range(4):
        nr = x + dr[i]
        nc = y + dc[i]
        if 0 <= nr < r and 0 <= nc < c:
            graph[nr][nc] = '.'
            timer[nr][nc] = 0

cnt = 1 # 초기 상태를 1초 지난 상태로 생각
while True:
    if cnt == n: # n초가 지난 경우라면
        break
    # 3번 과정
    graph = [['O'] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if timer[i][j] == 0: # 폭탄이 없는 곳이면 폭탄 설치
                timer[i][j] = 3
            else: # 기존에 폭탄이 있는 곳이라면 타이머 시간 -1
                timer[i][j] -= 1
    cnt += 1 # 1초 경과

    if cnt == n:
        break
    temp = [] # 터질 폭탄의 위치를 저장할 임시 리스트
    for i in range(r):
        for j in range(c):
            if timer[i][j] != 0: # 설치된 폭탄 타이머 -1
                timer[i][j] -= 1
            if timer[i][j] == 0: # 터질 폭탄이라면
                temp.append((i, j)) # 해당 위치를 temp에 저장
    for t in temp: # 저장된 위치에서 각각 폭발함수 실행
        explosion(t[0], t[1])
    cnt += 1 # 1초 경과

for i in range(r):
    print(''.join(graph[i]))