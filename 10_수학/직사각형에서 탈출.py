import sys
si = sys.stdin.readline

x, y, w, h = map(int, si().split())

print(min(x, y, w - x, h - y))