import sys
si = sys.stdin.readline

n = int(si())
length = n // 5
signal = [[0] * length for _ in range(5)]

temp = si().rstrip()
for i in range(len(temp)):
    if temp[i] == '#':
        signal[i // length][i % length] = 1

def check(index):
    if signal[4][index] == 1 and signal[0][index + 1] == 0:
        return '1'
    elif signal[2][index] == 1 and signal[2][index + 1] == 0 and signal[2][index + 2] == 1:
        return '0'
    elif signal[3][index + 2] == 0 and signal[4][index + 2] == 1:
        return '2'
    elif signal[1][index] == 0 and signal[2][index] == 1 and signal[3][index] == 0:
        return '3'
    elif signal[0][index + 1] == 0 and signal[0][index + 2] == 1:
        return '4'
    elif signal[1][index + 2] == 0 and signal[3][index] == 0:
        return '5'
    elif signal[1][index + 2] == 0 and signal[3][index] == 1:
        return '6'
    elif signal[2][index] == 0 and signal[2][index + 1] == 0 and signal[2][index + 2] == 1:
        return '7'
    elif signal[1][index] == 1 and signal[1][index + 2] == 1 and signal[2][index + 1] == 1 and signal[3][index] == 1 and signal[3][index + 2] == 1:
        return '8'
    else:
        return '9'

result = []
if n == 5:
    if signal[0][0] == 1:
        print(1)
elif n == 10:
    if signal[0][0] == 1 or signal[0][1] == 1:
        print(1)
else:
    for i in range(length):
        if signal[0][i] == 1:
            if i == 0:
                result.append(check(i))
            elif i < length - 2:
                if signal[0][i - 1] == 0 and signal[2][i - 1] == 0:
                    result.append(check(i))
            else:
                if signal[0][i - 1] == 0 and signal[2][i - 1] == 0:
                    result.append('1')

    print(''.join(result))