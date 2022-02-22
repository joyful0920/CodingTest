import sys
si = sys.stdin.readline

# 벽 길이 입력
n = int(si())

d = [0] * 31
d[0] = 1

for i in range(2, n + 1, 2):
    d[i] = d[i - 2] * 3
    for j in range(0, i - 2, 2):
        d[i] += d[j] * 2

print(d[n])