atmos = [[30, 15], [80, 35]]

def solution(atmos):
    answer = 0 # 사용한 마스크 갯수
    cnt = 0 # 사용중인 마스크의 첫 개시 후 경과한 날짜
    for i in atmos:
        if i[0] > 150 and i[1] > 75: # 미세먼지, 초미세먼지 모두 매우 나쁨
            if cnt == 0: # 새로운 마스크가 필요한 경우
                answer += 1
            cnt = 0 # 당일 착용 후 폐기
        elif i[0] > 80 or i[1] > 35: # 미세먼지, 초미세먼지 둘 중 하나 나쁨 이상
            if cnt == 0:
                answer += 1
            cnt += 1
            if cnt == 3: # 폐기해야하는 경우 (3일 경과)
                cnt = 0
        else: # 둘다 보통 이하
            if cnt != 0: # 사용 중인 마스크가 있다면 경과일 카운트
                cnt += 1
            if cnt == 3:
                cnt = 0
    return answer

print(solution(atmos))