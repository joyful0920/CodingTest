import sys
si = sys.stdin.readline

name = si().rstrip()

# 최종적으로 출력할 팰린드롬 = prefix + center + suffix(뒤집어서)
prefix = ''
suffix = ''
center = ''
temp = False

# 이름 길이가 홀수라면 알파벳 하나가 가운데에 혼자 들어갈 수 있음
def centering(i):
    global center, temp
    if not temp: # 아직 가운데 찬스를 안쓴 경우
        temp = True
        center = chr(i)
    else: # 이미 찬스를 쓴 경우
        print("I'm Sorry Hansoo")
        exit(0)

# 아스키 코드의 대문자 범위(65~90)만큼 반복
for i in range(65, 91):
    cnt = name.count(chr(i)) # 각각의 알파벳 개수 구하고
    if cnt >= 2 : # 2 이상이라면
        for _ in range(cnt // 2): # cnt의 절반만큼 전위와 후위에 알파벳 추가
            prefix += chr(i)
            suffix += chr(i)
        if cnt % 2 == 1: # 카운트값이 홀수라 하나 남는다면 centering 함수 실행
            centering(i)
    elif cnt == 1: # 카운트값이 1일 경우엔 바로 centering 함수 실행
        centering(i)

print(prefix + center + suffix[::-1])