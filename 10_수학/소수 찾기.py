import sys
si = sys.stdin.readline

n = int(si())
array = list(map(int, si().split()))
cnt = 0

def decimal(num, i):
    if num == 1:
        return None
    elif num % i != 0:
        return decimal(num, i + 1)
    else:
        if i < num:
            return None
        else:
            return num

for i in range(n):
    if decimal(array[i], 2) != None:
        cnt += 1

print(cnt)