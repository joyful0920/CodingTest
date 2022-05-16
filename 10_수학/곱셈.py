import sys
sys.setrecursionlimit(10**9)
si = sys.stdin.readline

a, b, c = map(int, si().split())

def cal(a, b):
    if b == 1:
        return a % c
    else:
        temp = cal(a, b // 2)
        if b % 2 == 0:
            return temp * temp % c
        else:
            return temp * temp * a % c

result = cal(a, b)
print(result)