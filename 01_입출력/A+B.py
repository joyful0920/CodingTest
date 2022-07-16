import sys
si = sys.stdin.readline

A, B = map(int, si().split())

def cal():
    total = A + B
    return total

print(cal())