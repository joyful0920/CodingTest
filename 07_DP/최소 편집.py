import sys
si = sys.stdin.readline

a = si().rstrip()
b = si().rstrip()
a_len = len(a)
b_len = len(b)

# a 길이+1을 행 길이로, b 길이+1을 열 길이로 2차원 DP 테이블 생성
dp = [[0] * (b_len + 1) for _ in range(a_len + 1)]

for i in range(a_len + 1):
    dp[i][0] = i # 첫 번째 열의 행 요소들 초기화
for i in range(b_len + 1):
    dp[0][i] = i # 첫 번째 행의 열 요소들 초기화

for i in range(1, a_len + 1):
    for j in range(1, b_len + 1):
        if a[i - 1] == b[j - 1]: # 비교하는 문자가 같을 경우
            dp[i][j] = dp[i - 1][j - 1] # 왼쪽 대각선 위 요소를 그대로 가져옴
        else: # 다를 경우
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1 # 교체, 삭제, 삽입하는 경우 중 최솟값을 저장

print(dp[a_len][b_len])