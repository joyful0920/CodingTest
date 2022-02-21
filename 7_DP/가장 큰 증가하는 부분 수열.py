import sys
si = sys.stdin.readline

# n과 수열 입력
n = int(si())
array = list(map(int, si().split()))

# 증가하는 부분 수열의 합을 담을 DP 테이블
d = array[:]

for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]:
            d[i] = max(d[i], d[j] + array[i])

# 가장 큰 증가하는 부분 수열 길이 출력
print(max(d))