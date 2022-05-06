import sys
si = sys.stdin.readline

n = int(si().rstrip())
formula = list(map(str, si().rstrip()))

nums = dict()
num = 64
for _ in range(n):
    num += 1
    nums[num] = int(si().rstrip())

stack = []
for f in formula:
    if 65 <= ord(f) <= 90:
        stack.append(nums[ord(f)])
    else:
        b = stack.pop(-1)
        a = stack.pop(-1)
        if f == '+':
            stack.append(a + b)
        elif f == '-':
            stack.append(a - b)
        elif f == '*':
            stack.append(a * b)
        else:
            stack.append(a / b)

print(format(stack[0], ".2f")) # 소숫점 2째자리까지 출력