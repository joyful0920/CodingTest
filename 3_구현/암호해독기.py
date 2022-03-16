import sys
si = sys.stdin.readline

n = int(si())
array = sorted(list(map(int, si().split())))
decoded = sorted(list(map(str, si().rstrip())))

def check(array, decoded):
    for i in range(n):
        if array[i] == 0:
            array[i] = ' '
        elif 1 <= array[i] <= 26:
            array[i] = chr(array[i] + 64)
        else:
            array[i] = chr(array[i] + 70)
        if array[i] != decoded[i]:
            return False
    return True

if check(array, decoded) == True:
    print('y')
else:
    print('n')