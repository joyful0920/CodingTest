import sys, math
si = sys.stdin.readline

m, n = map(int, si().split())

def prime_number(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

for i in range(m, n + 1):
    if prime_number(i) == True:
        print(i)