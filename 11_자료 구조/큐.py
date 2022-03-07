import sys
from collections import deque
si = sys.stdin.readline

n = int(si())
queue = deque()

def que(direct):
    # push
    if 'push' in direct:
        direct = direct.strip('push ')
        queue.append(direct)
    # pop
    elif direct == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    # size
    elif direct == 'size':
        print(len(queue))
    # empty
    elif direct == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    # front
    elif direct == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    # back
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

for _ in range(n):
    que(si().rstrip())