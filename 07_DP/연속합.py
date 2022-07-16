import sys
si = sys.stdin.readline

# n 입력
n = int(si())

# 수열 입력
array = list(map(int, si().split()))

d = [0] * n
d[0] = array[0]

for i in range(1, n):
    d[i] = max(array[i], d[i - 1] + array[i])

print(max(d))