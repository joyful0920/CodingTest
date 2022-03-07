import sys
from collections import deque
si = sys.stdin.readline

n = int(si())

array = deque([int(si()) for _ in range(n)])
nums = deque(sorted(list(array)))

stk = deque()
max_num = 0
result = deque()
temp = True

for i in array:
    if len(stk) == 0 or i > max_num:
        for _ in range(i - max_num):
            stk.append(nums.popleft())
            result.append('+')
        max_num = stk[-1]
        stk.pop()
        result.append('-')
    elif i == stk[-1]:
        stk.pop()
        result.append('-')
    elif i < max_num:
        if array[i] == stk[-1]:
            stk.pop()
            result.append('-')
        else:
            temp = False
            break

if temp == True:
    for i in result:
        print(i)
else:
    print('NO')