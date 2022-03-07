import sys
si = sys.stdin.readline

n = int(si())
array = []

for _ in range(n):
    x, y = map(int, si().split())
    array.append((x, y))

array.sort(key=lambda x:x[0])
array.sort(key=lambda x:x[1])

for i in range(n):
    print(array[i][0], array[i][1])