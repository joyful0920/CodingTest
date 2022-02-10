import sys
si = sys.stdin.readline

n = int(si())
array = list(map(int, si().split()))
array.sort()

print(array[0], array[-1])