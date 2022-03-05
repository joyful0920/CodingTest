import sys
si = sys.stdin.readline

n = int(si())
array = list(map(int, si().split()))
dic = dict()

m = int(si())
cards = list(map(int, si().split()))

for i in array:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in cards:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')