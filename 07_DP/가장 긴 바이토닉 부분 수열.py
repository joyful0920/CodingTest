import sys
si = sys.stdin.readline

# n과 수열 입력
n = int(si())
array = list(map(int, si().split()))

# 증가, 감소, 바이토닉 부분 수열 길이를 담을 DP 테이블
up = [1] * n
down = [1] * n
dp = [0] * n

# 증가하는 부분 수열 길이 계산
for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            up[i] = max(up[i], up[j] + 1)

# 감소하는 부분 수열 길이 계산
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if array[i] > array[j]:
            down[i] = max(down[i], down[j] + 1)


# 증가하는 부분 수열 길이와 감소하는 부분 수열 길이를 더해 바이토닉 수열 길이 계산
for i in range(n):
    dp[i] = up[i] + down[i] - 1

# 출력
print(max(dp))