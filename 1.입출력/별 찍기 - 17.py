import sys
si = sys.stdin.readline

n = int(si())

for i in range(0, n):
    if i == 0:
        print(' ' * (n - 1) + '*')
    elif i == n - 1:
        print('*' * (2 * n - 1)) 
    else:
        print(' ' * (n - i - 1) + '*' + ' ' * (2 * i - 1) + '*')