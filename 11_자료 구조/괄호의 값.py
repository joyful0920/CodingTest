import sys
si = sys.stdin.readline

s = si().rstrip()

stack = []
temp = 1
result = 0

for i in range(len(s)):
    if s[i] == '(': # 열린 괄호면 스택에 추가
        stack.append(s[i])
        temp *= 2 # 해당 괄호의 값만큼 temp에 곱해주기
    elif s[i] == '[':
        stack.append(s[i])
        temp *= 3
    elif s[i] == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break
        if s[i - 1] == '(': # 직전 괄호와 짝을 이룰 경우만
            result += temp # 현재의 temp를 결과값에 곱함
        stack.pop() # 연산이 끝난 괄호는 스택에서 제거
        temp //= 2 # 해당 괄호의 값만큼 temp를 나눠줌으로써 연산 처리
    else:
        if not stack or stack[-1] == '(':
            result = 0
            break
        if s[i - 1] == '[':
            result += temp
        stack.pop()
        temp //= 3

if stack: # 스택에 요소가 남아있다면 불균형 스트링
    print(0)
else:
    print(result)
