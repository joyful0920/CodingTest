import sys
from collections import deque
si = sys.stdin.readline

n = int(si())
arr = deque(int(si()) for _ in range(n))
sorted_arr = deque(sorted(arr))
stack = deque()
result = []

last = 0
temp = True
while arr:
    if last < arr[0]:
        last = sorted_arr.popleft()
        stack.append(last)
        result.append('+')
    elif last == arr[0]:
        arr.popleft()
        stack.pop()
        result.append('-')
    else:
        if stack.pop() == arr.popleft():
            result.append('-')
        else:
            temp = False
            break

if temp:
    for i in result:
        print(i)
else:
    print('NO')