import sys
si = sys.stdin.readline

n = int(si())
array = set()

for _ in range(n):
    array.add(int(si()))

array = sorted(list(array))

for i in range(n):
    print(array[i])