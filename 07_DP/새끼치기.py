import sys
si = sys.stdin.readline

n = int(si())

d = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1:
        d[1] = 1
    elif i == 2:
        d[2] = 2
    elif i == 3:
        d[3] = 4
    elif i == 4:
        d[4] = 7
    elif i % 2 == 1:
        d[i] = d[i - 1] * 2
    else:
        d[i] = d[i - 1] * 2 - d[i - 5] - d[i - 4]

print(d[n])