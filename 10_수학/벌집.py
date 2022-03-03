import sys
si = sys.stdin.readline

n = int(si())
sum = 1

for i in range(0, n):
    sum += 6 * i
    if sum >= n:
        print(i + 1)
        break