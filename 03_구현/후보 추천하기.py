import sys
si = sys. stdin.readline

n = int(si())
rec = int(si())
num = list(map(int, si().split()))

photo = dict()
for i in range(rec):
    if num[i] in photo: # 딕셔너리에 존재하는 경우(게시된)
        photo[num[i]][0] += 1 # 해당 학생의 추천수 +1
    else: # 게시되지 않은 사진이라면
        if len(photo) < n: # 사진 추가가 가능하다면 추가
            photo[num[i]] = [1, i] # [추천수, 추가된 순서]
        else:
            temp = sorted(photo.items(), key = lambda x : (x[1][0], x[1][1])) # 추천수와, 추가된 순으로 오른차순 정렬
            del(photo[temp[0][0]]) # 가장 앞에 있는 요소 삭제
            photo[num[i]] = [1, i] #

result = list(sorted(photo.keys())) # 키값(학생번호)로 정렬
print(*result)