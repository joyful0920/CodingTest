import sys
si = sys.stdin.readline

A = int(si().rstrip())
B = int(si().rstrip())

def cal():
    total = A + B
    return total

print(cal())