import sys
from collections import deque
si = sys.stdin.readline

n, k = map(int, si().split())
deq = deque()
array = []

for i in range(1, n + 1):
    deq.append(i)

for i in range(n):
    deq.rotate(-k + 1)
    array.append(str(deq.popleft()))

print('<' + ', '.join(array) + '>')