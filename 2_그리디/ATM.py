import sys
si = sys.stdin.readline

n = int(si())
times = sorted(list(map(int, si().split())))

result = 0
for i in range(1, n + 1):
    for j in range(i):
        result += times[j]

print(result)