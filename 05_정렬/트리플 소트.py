import sys
si = sys.stdin.readline

n = int(si())
array = list(map(int, si().split()))
ok = True

for i in range(n):
    if i % 2 == 0:
        if array[i] % 2 == 0:
            ok = False

if ok:
    print('YES')
else:
    print('NO')