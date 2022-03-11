import sys
from collections import deque
si = sys.stdin.readline

n = int(si())
s = set()

for _ in range(n):
    cmd = si().rstrip().split()
    
    if len(cmd) == 1:
        if cmd[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
    else:
        cmd, num = cmd[0], int(cmd[1])
        if cmd == 'add':
            s.add(num)
        elif cmd == 'remove':
            s.discard(num)
        elif cmd == 'check':
            if num in s:
                print(1)
            else:
                print(0)
        elif cmd == 'toggle':
            if num in s:
                s.discard(num)
            else:
                s.add(num)