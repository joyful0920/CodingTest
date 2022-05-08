import sys
si = sys.stdin.readline

n = int(si())
array = list(map(int, si().split()))

stack = []
result = []

for i in range(n):
    while stack:
        if stack[-1][1] > array[i]: # 수신 가능
            result.append(stack[-1][0] + 1)
            break
        else: # 수신 불가능한 탑은(현재 탑보다 낮음)
            stack.pop() # 스택에서 삭제
    if not stack: # 빈 스택은 수신할 탑 자체가 없음을 의미
        result.append(0) # 최종적으로 수신 불가
    stack.append((i, array[i])) # 마지막 검사 탑을 스택에 삽입

print(*result)