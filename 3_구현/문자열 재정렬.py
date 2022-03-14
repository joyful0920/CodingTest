import sys
si = sys.stdin.readline

# 입력받은 문자열을 하나씩 쪼개서 정렬시킨 후 리스트에 저장
s = sorted(list(map(str, si().rstrip())))
num = 0 # 숫자를 더할 변수
result = '' # 결과값을 출력에 사용할 변수

for i in s:
    if i.isdigit() == True: # 숫자 판별을 위해 isdigit() 함수 사용
        num += int(i) # 숫자면 num에 더하고
    else:
        result += i # 문자면 result에 더하기

# 만든 문자열과 더한 숫자를 연결하여 출력
print(result + str(num))