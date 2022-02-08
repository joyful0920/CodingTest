import sys
si = sys.stdin.readline

# 정수 X 입력
x = int(si().rstrip())
cnt = 0

# 탑다운 DP
def makeOne(x):
    global cnt
    # 몫 5로 나누어 떨어지는 경우를 추가
    # 루트?
    if # 5의 거듭제곱인지 판별하는 조건문
        cnt += 1
        return (makeOne(x / 5))
    elif # 3의 거듭제곱인지 판별하는 조건문
        cnt += 1
        return (makeOne(x / 3))
    elif (x & (x - 1) == 0): # 2의 거듭제곱인지 판별
        cnt += 1
        return (makeOne(x / 2))
    elif (x - 1) != 0:
        cnt += 1
        return (makeOne(x - 1)) # 26 - 1= 25
    else:
        return cnt # min

print(makeOne(x))