import sys
si = sys.stdin.readline

n = int(si())
array = []
rank = [1] * n

for _ in range(n):
    x, y = map(int, si().split())
    array.append((x, y))

for i in range(n):
    for j in range(n):
        if array[i][0] < array[j][0] and array[i][1] < array[j][1]:
            rank[i] += 1

for i in range(n):
    print(rank[i], end=' ')