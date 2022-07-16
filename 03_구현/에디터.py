import sys
from collections import deque
si = sys.stdin.readline

stack1 = deque(map(str, si().rstrip()))
stack2 = deque()

m = int(si())
for _ in range(m):
    command = list(map(str, si().rstrip()))
    if command[0] == 'L':
        if stack1:
            stack2.appendleft(stack1.pop())
    elif command[0] == 'D':
        if stack2:
            stack1.append(stack2.popleft())
    elif command[0] == 'B':
        if stack1:
            stack1.pop()
    else:
        stack1.append(command[2])

stack1.extend(stack2)
print(''.join(stack1))