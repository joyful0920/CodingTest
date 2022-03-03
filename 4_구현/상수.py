import sys
si = sys.stdin.readline

a, b = map(str, si().split())

a = int("".join(reversed(a)))
b = int("".join(reversed(b)))

print(max(a, b))