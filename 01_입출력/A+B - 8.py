import sys
si = sys.stdin.readline

t = int(si())

for i in range(1, t + 1):
    a, b = map(int, si().split())
    print(f'Case #{i}: {a} + {b} = {a + b}')