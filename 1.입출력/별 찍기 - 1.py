import sys
si = sys.stdin.readline

n = int(si())
star = ['*'] * (n + 1)

for i in range(1, n + 1):
    print(star[:i])
