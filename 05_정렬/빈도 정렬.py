from re import X
import sys
si = sys.stdin.readline

n, c = map(int, si().split())
array = list(map(int, si().split()))

count = dict()
num = []
temp = []

for i in array:
    if not i in num:
        count[i] = 1
        num.append(i)
    else:
        count[i] += 1

for i in range(len(num)):
    temp.append((count[num[i]], i, num[i]))

temp.sort(key = lambda x : (-x[0], x[1], x[2]))

result = []
for i in temp:
    for _ in range(i[0]):
        result.append(i[2])

print(*result)