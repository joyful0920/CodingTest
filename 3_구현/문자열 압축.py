import sys
si = sys.stdin.readline

s = si().rstrip()
results = [] # 각 단위로 자른 결과의 문자열 길이를 담을 리스트

# 1부터 문자열 길이만큼 반복
for i in range(1, len(s) + 1):

    # 문자열을 자르기
    sliced = [] # 각 단위로 자른 문자열을 담을 리스트
    for j in range(0, len(s), i):
        sliced.append(s[j:j + i])

    # 현재 문자열과 그 전 문자열을 비교
    temp = [] # 중복된 문자열을 제거한 요소를 담을 리스트
    num = [] # 반복되는 문자열을 카운트한 숫자를 담을 리스트
    cnt = 1
    for x in range(1, len(sliced)):
        if sliced[x] == sliced[x - 1]: # 같다면 카운트 + 1
            cnt += 1
        else: # 다르다면 직전 문자열을 temp에 저장
            temp.append(sliced[x - 1])
            if cnt == 1: # 카운트 횟수가 1이라면 ''로 변환
                cnt = ''
            num.append(cnt) # 카운트 횟수를 num에 저장
            cnt = 1

    # 누락된 마지막 요소들을 추가할 코드
    temp.append(sliced[-1])            
    if cnt == 1:
        cnt = ''
    num.append(cnt)

    # temp와 num의 요소를 합친 후 result에 연결
    result = '' # 압축한 문자열을 저장할 변수
    for y in range(len(num)):
        result += (str(num[y]) + temp[y])
    
    # 압축된 문자열의 길이를 results에 저장
    results.append(len(result))

# 압축된 문자열의 최소 길이 출력
print(min(results))