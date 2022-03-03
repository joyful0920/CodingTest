import sys
si = sys.stdin.readline

a = int(si())
b = int(si())
c = int(si())
result = str(a * b * c)

array = [0] * 10

for i in range(len(result)):
    array[int(result[i])] += 1

for i in range(len(array)):
    print(array[i])