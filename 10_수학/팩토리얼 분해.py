import sys
si = sys.stdin.readline

n = int(si())
f = 2432902008176640000

if n == 0:
    print('NO')
    exit()

for i in range(20, 0, -1):
    f //= i
    if n >= f:
        n -= f

if n == 0:
    print('YES')
else:
    print('NO')