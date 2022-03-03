import sys
si = sys.stdin.readline

result = []

while(True):
    array = list(map(int, si().split()))
    array.sort()
    if array[0] == 0 and array[1] == 0 and array[2] == 0:
        break
    elif array[-1] ** 2 == array[0] ** 2 + array[1] ** 2:
        result.append('right')
    else:
        result.append('wrong')

for i in range(len(result)):
    print(result[i])