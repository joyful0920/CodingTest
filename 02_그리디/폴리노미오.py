import sys
si = sys.stdin.readline

# 리스트 형태로 보드판의 요소를 저장
board = list(map(str, si().rstrip()))
cnt = 0

# 폴리오미노 함수
def polyomino(i):
    if cnt % 2 == 1:
            print(-1)
            exit(0)
    elif cnt % 4 == 2:
        board[i - 1] = 'B'
        board[i - 2] = 'B'

# 보드판 전체 탐색
for i in range(len(board)):
    if board[i] == 'X': # X가 나오면 일단 모두 A로 덮어주기
        board[i] = 'A'
        cnt += 1
    else: # .가 나올 경우
        polyomino(i)
        cnt = 0

# 마지막이 X로 끝날 경우를 대비해 한번 더 폴리오미노 함수 실행
polyomino(0)

for i in board:
    print(i, end = '')