import sys
si = sys.stdin.readline

n = int(si())
array = []

for _ in range(n):
    a, b = map(str, si().rstrip().split())
    array.append((int(a), b))

array.sort(key=lambda x:x[0])

for i in range(n):
    print(array[i][0], array[i][1])