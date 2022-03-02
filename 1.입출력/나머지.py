import sys
si = sys.stdin.readline

array = []

for _ in range(10):
    num = int(si())
    array.append(num % 42)

s = set(array)

print(len(s))