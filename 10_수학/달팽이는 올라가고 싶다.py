import sys
si = sys.stdin.readline

a, b, v = map(int, si().split())

def cal(a, b, v):
    a -= b
    v -= b
    if v % a != 0:
        date = v // a + 1
    else:
        date = v // a
    return date

print(cal(a, b, v))