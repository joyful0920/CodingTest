import sys
si = sys.stdin.readline

nums = [list(map(str, si().split())) for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, n):
    if len(n) == 6:
        if n not in result:
            result.append(n)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, n + nums[nx][ny])

result = []
for i in range(5):
    for j in range(5):
        dfs(i, j, nums[i][j])

print(len(result))