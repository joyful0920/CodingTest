import sys
si = sys.stdin.readline

array = list(map(int, si().split()))
total = 0

for i in range(len(array)):
    total += array[i] ** 2

print(total % 10)