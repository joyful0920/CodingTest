import sys
from collections import deque
si = sys.stdin.readline

n = int(si())
queue = deque([i for i in range(1, n + 1)])

while(len(queue) > 1):
    queue.popleft()
    temp = queue.popleft()
    queue.append(temp)

print(queue[0])