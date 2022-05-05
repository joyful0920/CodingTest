import sys
si = sys.stdin.readline

n = int(si())
board = [list(map(str, si().rstrip())) for _ in range(n)]

# 열 교환 함수
def change_c(x, y):
    temp = board[x][y]
    board[x][y] = board[x][y + 1]
    board[x][y + 1] = temp

# 행 교환 함수
def change_r(x, y):
    temp = board[i][y]
    board[x][y] = board[x + 1][y]
    board[x + 1][y] = temp

# 같은 사탕으로 이뤄진 행, 열 길이 카운트 함수
def count():
    result = 0
    for i in range(n):
        cnt = 1
        for j in range(n - 1):
            if board[i][j] == board[i][j + 1]:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 1
    for j in range(n):
        cnt = 1
        for i in range(n - 1):
            if board[i][j] == board[i + 1][j]:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 1
    return result

result = 0
for i in range(n): # 열에 대한 교환 및 카운트 수행
    for j in range(n - 1):
        if board[i][j] != board[i][j + 1]:
            change_c(i, j)
            result = max(result, count())
            change_c(i, j)

for j in range(n): # 행에 대한 교환 및 카운트 수행
    for i in range(n - 1):
        if board[i][j] != board[i + 1][j]:
            change_r(i, j)
            result = max(result, count())
            change_r(i, j)

print(result)