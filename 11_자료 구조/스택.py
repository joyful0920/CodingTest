import sys
from collections import deque
si = sys.stdin.readline

n = int(si())

stk = deque()

def stack(direct):
    # push
    if 'push' in direct:
        direct = direct.strip('push ')
        stk.append(direct)
    # push
    elif direct == 'pop':
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.pop())
    # size
    elif direct == 'size':
        print(len(stk))
    # empty
    elif direct == 'empty':
        if len(stk) == 0:
            print(1)
        else:
            print(0)
    # top
    else:
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1])

for _ in range(n):
    stack(si().rstrip())