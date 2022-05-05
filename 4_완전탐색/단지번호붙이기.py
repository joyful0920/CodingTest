import sys
si = sys.stdin.readline

n = int(si())
graph = [list(map(int, si().rstrip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def dfs(x, y):
    if 0 <= x < n and 0 <= y < n and graph[x][y] == 1 and not visited[x][y]:
        global cnt
        cnt += 1
        visited[x][y] = True
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True

result = []
for i in range(n):
    for j in range(n):
        cnt = 0
        if dfs(i, j):
            result.append(cnt)

result.sort()
print(len(result))
for i in result:
    print(i)