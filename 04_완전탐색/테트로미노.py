import sys
si = sys.stdin.readline

n, m = map(int, si().split())
paper = [list(map(int, si().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 상하좌우 탐색에 사용할 방향 인덱스 배열
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 종이에서 가장 큰 값
max_val = max(map(max, paper))

# 결과값을 저장할 변수
result = 0

# DFS 함수
def dfs(x, y, cnt, total):
    global result
    # 남은 탐색 지점을 모두 최댓값으로 해도 현재까지의 result보다 작으면 해당 탐색은 조기종료
    if result >= total + max_val * (4 - cnt):
        return
    # 4개의 도형을 모두 사용했다면
    if cnt == 4:
        result = max(result, total) # result값 갱신
    else: # 아직 도형을 다 사용못한 경우
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                # ㅜ, ㅗ, ㅏ, ㅓ 모양을 만들기 위한 반례 처리
                if cnt == 2:
                    visited[nx][ny] = True # nx, ny 좌표는 방문 처리하고
                    dfs(x, y, cnt + 1, total + paper[nx][ny]) # x, y에서 다시 탐색 수행
                    visited[nx][ny] = False
                visited[nx][ny] = True
                dfs(nx, ny, cnt + 1, total + paper[nx][ny])
                visited[nx][ny] = False

# 종이 2차원 배열 모든 요소에서 DFS 수행
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, paper[i][j])
        visited[i][j] = False

print(result)