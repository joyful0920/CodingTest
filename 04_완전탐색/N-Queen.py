n = int(input())
row = [0] * n # row[행] = 열
visited = [0] * n
result = 0

def check(x):
    for i in range(x): # 현재 열 윗열에 위치한 퀸들이
        if row[x] == row[i] or abs(x - i) == abs(row[x] - row[i]): # 같은 열이거나 대각선에 위치한다면
            return False
    return True

def dfs(x):
    global result
    if x == n: # 끝 범위까지 탐색이 진행된 경우
        result += 1
        return
    else:
        for i in range(n): # 현재 탐색 중인 행의 모든 열들을 테스트
            if visited[i] == 0: # 퀸이 놓여있지 않은 행이라면
                row[x] = i
                if check(x): # 가능한 열이 있다면 다음 행 탐색
                    visited[i] = 1 # 행 방문처리
                    dfs(x + 1)
                    visited[i] = 0 # 하나의 dfs 케이스가 끝나면 다시 미방문처리

dfs(0)
print(result)