import sys
si = sys.stdin.readline

t = int(si())

for _ in range(t):
    h, w, n = map(int, si().split())
    if n % h == 0:
        floor = h
        num = n // h
    else:
        floor = n % h
        num = n // h + 1
    if num < 10:
        print(str(floor) + '0' + str(num))
    else:
        print(str(floor) + str(num))