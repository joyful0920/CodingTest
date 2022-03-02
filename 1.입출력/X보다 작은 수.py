import sys
si = sys.stdin.readline

n, x = map(int, si().split())

array = list(map(int, si().split()))
result = []
for i in range(n):
    if array[i] < x:
        result.append(array[i])

for i in range(len(result)):
    print(result[i], end= ' ')