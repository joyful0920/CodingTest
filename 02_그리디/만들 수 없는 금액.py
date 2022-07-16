import sys
si = sys.stdin.readline

n = int(si())
array = list(map(int, si().split()))
array.sort()
target = 1

for i in array:
    if target < i:
        break
    target += i

print(target)