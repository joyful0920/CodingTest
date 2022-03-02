import sys
si = sys.stdin.readline

array = [int(si().rstrip()) for _ in range(9)]

max = array[0]
index = 0

for i in range(9):
    if array[i] > max:
        max = array[i]
        index = i

print(max)
print(index + 1)