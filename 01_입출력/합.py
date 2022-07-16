import sys
si = sys.stdin.readline

n = int(si())
total = 0

for i in range(1, n + 1):
    total += i

print(total)