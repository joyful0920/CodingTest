import sys
si = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(si())
mines = [int(si()) for _ in range(n)]
exploded = [False] * n # 지뢰 폭발 여부를 체크하기 위한 배열
result = []

# 폭발 함수
def explode(index):
    # 현재 인덱스의 왼쪽 옆 지뢰 체크
    if index - 1 >= 0 and exploded[index - 1] == False: # 왼쪽 옆 인덱스가 0 이상이고, 터지지 않은 지뢰라면
        if mines[index] > mines[index - 1]: # 현재 지뢰의 폭발 힘이 왼쪽 지뢰보다 큰 경우에만
            exploded[index - 1] = True # 왼쪽 지뢰 폭발
            explode(index - 1) # 폭발한 왼쪽 지뢰 기준으로 폭발 함수 재호출
    # 현재 인덱스의 오른쪽 옆 지뢰 체크            
    if index + 1 <= n - 1 and exploded[index + 1] == False: # 오쪽 옆 인덱스가 n - 1 이하이고, 터지지 않은 지뢰라면
        if mines[index] > mines[index + 1]: # 현재 지뢰의 폭발 힘이 오른쪽 지뢰보다 큰 경우에만
            exploded[index + 1] = True # 오른쪽 지뢰 폭발
            explode(index + 1) # 폭발한 오른쪽 지뢰 기준으로 폭발 함수 재호출

if n == 1: # 반례 처리 : 지뢰 개수가 1일 경우
    print(1)
else:
    for i in range(n):
        if i == 0: # 맨 왼쪽 지뢰일 경우
            if mines[i] >= mines[i + 1] and exploded[i] == False: # 오른쪽 옆 지뢰 확인
                exploded[i] == True # 조건을 만족하면 폭발
                result.append(i + 1) # 결과 리스트에 폭발한 지뢰 번호 저장
                explode(i) # 폭발한 지뢰 기준으로 폭발 함수 실행
        elif i == n - 1: # 맨 오른쪽 지뢰일 경우
            if mines[i] >= mines[i - 1] and exploded[i] == False: # 왼쪽 옆 지뢰 확인
                exploded[i] == True
                result.append(i + 1)
                explode(i)
        else: # 그 외의 경우
            if mines[i - 1] <= mines[i] >= mines[i + 1] and exploded[i] == False: # 해당 지뢰의 폭발 힘이 양쪽 지뢰보다 큰 경우만
                exploded[i] == True
                result.append(i + 1)
                explode(i)

    # 결과 리스트에 저장된 지뢰 번호 정렬
    result.sort()

    for i in result:
        print(i)