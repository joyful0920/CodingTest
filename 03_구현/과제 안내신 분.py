import sys
si = sys.stdin.readline

array = [0] * 31

for _ in range(28):
    num = int(si())
    array[num] = 1

for i in range(1, 31):
    if array[i] == 0:
        print(i)