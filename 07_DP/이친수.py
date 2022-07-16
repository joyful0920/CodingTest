import sys
si = sys.stdin.readline

n = int(si())

d = [0] * (91)

d[1] = 1
d[2] = 1
d[3] = 2

for i in range(4, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])