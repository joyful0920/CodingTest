import sys
si = sys.stdin.readline

n = int(si())

for i in range(1, 10):
    print(f'{n} * {i} = {n * i}')