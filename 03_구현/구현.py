import sys
si = sys.stdin.readline

n = int(si())
length = n // 5
signal = [[0] * length for _ in range(5)] # 시그널을 5줄로 만들고 모두 0으로 초기화

temp = si().rstrip()
for i in range(len(temp)):
    if temp[i] == '#': # 시그널이 #인 경우 1로 재설정
        signal[i // length][i % length] = 1

def check(index): # 0~9를 특정할 수 있는 조건을 만족할 경우 해당 숫자를 반환
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
if n == 5: # 시그널 길이가 5인 경우 숫자 1만 가능
    if signal[0][0] == 1:
        print(1)
elif n == 10: # 시그널 길이가 10인 경우도 숫자 1만 가능
    if signal[0][0] == 1 or signal[0][1] == 1:
        print(1)
else:
    for i in range(length):
        if signal[0][i] == 1: # 시그널이 # == 1일 경우
            if i == 0: # 맨 왼쪽에 위치한 시그널일 경우
                result.append(check(i)) # 체크함수 실행
            elif i < length - 2: # 맨왼쪽도 맨 오른쪽도 아닌 경우
                if signal[0][i - 1] == 0 and signal[2][i - 1] == 0: #바로 왼쪽 옆줄이 공백인지 확인
                    result.append(check(i)) # 체크함수 실행
            else: # 맨 오른쪽 시그널일 경우
                if signal[0][i - 1] == 0 and signal[2][i - 1] == 0: # 바로 왼쪽 옆이 공백일 땐
                    result.append('1') # 숫자 1 특정 가능

    print(''.join(result))