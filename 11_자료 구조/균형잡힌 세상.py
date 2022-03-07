import sys
from collections import deque
si = sys.stdin.readline

while True:
    stk = deque()
    sentence = si().rstrip()
    temp = True
    if sentence == '.':
        break
    for i in sentence:
        if i == '(' or i == '[':
            stk.append(i)
        elif i == ')':
            if len(stk) == 0 or stk[-1] == '[':
                temp = False
                break
            else:
                stk.pop()
        elif i == ']':
            if len(stk) == 0 or stk[-1] == '(':
                temp = False
                break
            else:
                stk.pop()
    if len(stk) == 0 and temp == True:
        print('yes')
    else:
        print('no')