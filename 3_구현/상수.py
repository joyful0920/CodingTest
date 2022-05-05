import sys
si = sys.stdin.readline

a, b = map(str, si().split())

a = int(a[::-1])
b = int(b[::-1])

print(max(a, b))