import sys
si = sys.stdin.readline

# n과 수열 입력
n = int(si())
array = list(map(int, si().split()))

# 감소하는 부분 수열 길이를 담을 DP 테이블
d = [1] * n

for i in range(n):
    for j in range(i):
        if array[i] < array[j]:
            d[i] = max(d[i], d[j] + 1)

# 가장 긴 감소하는 부분 수열 길이 출력
print(max(d))
