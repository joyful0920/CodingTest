import sys
si = sys.stdin.readline

s = si().rstrip()
result = 0

for i in s:
    if i == '0' or i == '1':
        result += int(i)
    else:
        if result == 0:
            result += int(i)
        else:
            result *= int(i)

print(result)