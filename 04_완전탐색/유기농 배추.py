import sys
si = sys.stdin.readline
sys.setrecursionlimit(10**9)
t = int(si())

def dfs(x, y):
    if 0 <= x < m and 0 <= y < n and graph[x][y] == 1:
        graph[x][y] = 0    
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True

for _ in range(t):
    m, n, k = map(int, si().split())
    graph = [[0] * n for _ in range(m)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, si().split())
        graph[x][y] = 1

    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                cnt += 1
        
    print(cnt)