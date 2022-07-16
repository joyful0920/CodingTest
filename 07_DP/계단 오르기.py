import sys
si = sys.stdin.readline

# 계단 개수 입력
n = int(si())

# 계단 점수 입력
array = [int(si().rstrip()) for _ in range(n)]

# 얻을 수 있는 점수의 합을 저장할 DP 테이블
d = [0] * n

for i in range(n):
    if i == 0:
        d[0] = array[0]
    elif i == 1:
        d[1] = array[0] + array[1]
    elif i == 2:
        d[2] = max(array[0] + array[2], array[1] + array[2])
    else:
        d[i] = max(d[i - 2] + array[i], d[i - 3] + array[i - 1] + array[i])

print(d[n - 1])