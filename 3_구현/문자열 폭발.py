import sys
si = sys.stdin.readline

string = si().rstrip()
bomb = si().rstrip()

stack = []
for s in string:
    stack.append(s)
    # 현재 문자가 폭발문자열의 마지막 문자와 같고
    if s == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb: # 스택에 마지막 저장된 문자들로 폭발 문자열을 만들 수 있다면
        del stack[-len(bomb):] # 해당 문자열 삭제

result = ''.join(stack)

if result == '':
    print("FRULA")
else:
    print(result)