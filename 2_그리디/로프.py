import sys
from collections import deque
si = sys.stdin.readline

n = int(si())
array = sorted(deque([int(si()) for _ in range(n)]))
max_weight = -1

for i in range(len(array)):
    weight = array[i] * (len(array) - i)
    max_weight = max(max_weight, weight)

print(max_weight)