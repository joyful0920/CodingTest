import sys
sys.setrecursionlimit(10**9)
si = sys.stdin.readline

def dfs(x, y):
    if 0 <= x < h and 0 <= y < w and graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x - 1, y - 1)
        dfs(x - 1, y + 1)
        dfs(x + 1, y - 1)
        dfs(x + 1, y + 1)
        return True

while True:
    w, h = map(int, si().split())
    if w == 0 and h == 0:
        exit(0)
    
    graph = [list(map(int, si().split())) for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if dfs(i, j):
                cnt += 1
    
    print(cnt)