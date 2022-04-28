import sys
si = sys.stdin.readline

words = si().rstrip()
result = ""
stack = ""
temp = False

for i in words:
    if i == '<':
        temp = True # temp 스위칭
        result += stack[::-1] # 스택에 있던 문자열을 뒤집어서 result에 붙여주기
        stack = ""
        result += i
        continue
    elif i == '>':
        temp = False # temp 스위칭
        result += i
        continue
    elif i == ' ':
        result += stack[::-1] + ' ' # 스택에 문자열이 있다면 뒤집어서 result에 붙여주기
        stack = ""
        continue

    if temp: # True
        result += i
    else: # False
        stack += i

print(result + stack[::-1])