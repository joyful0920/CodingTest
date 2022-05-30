import sys
si = sys.stdin.readline

s = si().rstrip()
result = 0

for i in s:
    i = int(i)
    if i == 0 or i == 1: # 문자 i가 0 또는 1인 경우
        result += i
    else:
        if result == 0: # result 값이 0인 경우 곱하면 손해
            result += i
        else:
            result *= i

print(result)