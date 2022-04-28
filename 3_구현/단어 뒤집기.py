import sys
si = sys.stdin.readline

t = int(si())

for _ in range(t):
    words = list(map(str, si().rstrip().split()))
    for word in words:
        print(word[::-1], end = " ")