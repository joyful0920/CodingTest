import sys
si = sys.stdin.readline

t = int(si())

for _ in range(t):
    r, s = map(str, si().rstrip().split())
    r = int(r)
    for i in range(len(s)):
        for _ in range(r):
            print(s[i], end='')
    print()