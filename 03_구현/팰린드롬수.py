import sys
si = sys.stdin.readline
array = []

def yesno(i):
    result = 'yes'
    for x in range(len(array[i]) // 2):
        if array[i][x] != array[i][-x -1]:
            result = 'no'
            break
    return result

while(True):
    num = list(map(str, str(si().rstrip())))
    if len(num) == 1 and num[0] == '0':
        break
    array.append(num)

for i in range(len(array)):
    if array[i][0] == '0':
        print('no')
    else:
        print(yesno(i))