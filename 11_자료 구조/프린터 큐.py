import sys
from collections import deque
si = sys.stdin.readline

t = int(si())

for _ in range(t):
    m, n = map(int, si().split())
    array = deque(list(map(int, si().split())))
    queue = deque([(array[i], i) for i in range(m)])
    result = deque()
    while len(array) != 0:
        if array[0] == max(array):
            array.popleft()
            result.append(queue.popleft())
        else:
            array.append(array.popleft())
            queue.append(queue.popleft())
    for i in range(m):
        if result[i][1] == n:
            print(i + 1)
            break