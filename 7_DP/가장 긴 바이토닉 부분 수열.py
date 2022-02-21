import sys
si = sys.stdin.readline

# n과 수열 입력
n = int(si())
array = list(map(int, si().split()))

# 증가, 감소, 바이토닉 부분 수열 길이를 담을 DP 테이블
d = [1] * n
p = [1] * n
t = [0] * n

# 증가하는 부분 수열 길이 계산
for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            d[i] = max(d[i], d[j] + 1)

# 감소하는 부분 수열 길이 계산
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if array[i] > array[j]:
            p[i] = max(p[i], p[j] + 1)


# 증가하는 부분 수열 길이와 감소하는 부분 수열 길이를 더해 바이토닉 수열 길이 계산
for i in range(n):
    t[i] = d[i] + p[i] - 1

# 출력
print(max(t))