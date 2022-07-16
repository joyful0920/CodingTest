from collections import deque
import sys
si = sys.stdin.readline

n = int(si())
m = int(si())

if m != 0:
    broken = deque(si().split())
else:
    broken = deque()

result = abs(n - 100)

for i in range(1000000):
    for j in range(len(str(i))):
        if str(i)[j] in broken:
            break
        elif j == len(str(i)) - 1:
            result = min(result, len(str(i)) + abs(n - i))

print(result)