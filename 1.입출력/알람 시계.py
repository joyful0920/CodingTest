import sys
si = sys.stdin.readline

h, m = map(int, si().split())

if m - 45 < 0:
    m = m + 15
    if h - 1 < 0:
        h = h + 23
    else:
        h -= 1
else:
    m -= 45

print(h, m)