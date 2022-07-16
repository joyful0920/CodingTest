import sys
si = sys.stdin.readline

# n 입력
n = int(si())

d = [i for i in range (n + 1)]

for i in range(1, n + 1):
    for j in range(1, i):
        if j * j > i:
            break
        if d[i - j * j] + 1 < d[i]:
            d[i] = d[i - j * j] + 1

print(d[n])