import sys
si = sys.stdin.readline

t = int(si())

for _ in range(t):
    ps = si().rstrip()
    sum = 0
    for i in ps:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print("YES")