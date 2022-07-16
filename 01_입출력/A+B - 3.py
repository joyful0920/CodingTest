import sys
si = sys.stdin.readline

n = int(si().rstrip())
array = []

for i in range(n):
    a, b = map(int, si().split())
    array.append(int(a + b))

for i in range(n):
    print(array[i])