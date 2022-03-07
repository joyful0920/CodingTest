import sys
from collections import deque
si = sys.stdin.readline

n = int(si())
q = deque()

def deq(direct):
    # push_front
    if 'push_front ' in direct:
        direct = direct.strip('push_front ')
        q.appendleft(direct)
    # push_back
    elif 'push_back ' in direct:
        direct = direct.strip('push_back ')
        q.append(direct)
    # pop_front
    elif direct == 'pop_front':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    # pop_back
    elif direct == 'pop_back':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    # size
    elif direct == 'size':
        print(len(q))
    # empty
    elif direct == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    # front
    elif direct == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    # back
    else:
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])

for _ in range(n):
    deq(si().rstrip())