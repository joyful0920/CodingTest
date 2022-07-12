import sys
sys.setrecursionlimit(10**9)
si = sys.stdin.readline

# DFS 함수
def dfs(x, y, target):
    if 0 <= x < n and 0 <= y < n and graph[x][y] == target and not visited[x][y]:
        visited[x][y] = True
        dfs(x - 1, y, target)
        dfs(x + 1, y, target)
        dfs(x, y - 1, target)
        dfs(x, y + 1, target)
        return True

# 카운트 함수
def counting(blind):
    global visited
    visited = [[False] * n for _ in range(n)]
    cnt = 0

    # 적록색약의 경우
    if blind:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'R':
                    graph[i][j] = 'G'

    for i in range(n):
        for j in range(n):
            if dfs(i, j, graph[i][j]) == True:
                cnt += 1
    return cnt
    
n = int(si())
graph = [list(map(str, si().rstrip())) for _ in range(n)]

print(counting(False), counting(True))