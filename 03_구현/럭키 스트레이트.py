import sys
si = sys.stdin.readline

n = si().rstrip()
first = 0
second = 0

# 문자열을 절반으로 나눴을 때 앞부분의 합
for i in range(len(n) // 2):
    first += int(n[i])

# 문자열을 절반으로 나눴을 때 뒷부분의 합
for i in range(-1, -(len(n) // 2) - 1, -1):
    second += int(n[i])

# 앞부분과 뒷부분의 합이 같을 때만 LUCKY 출력
if first == second:
    print('LUCKY')
else:
    print('READY')