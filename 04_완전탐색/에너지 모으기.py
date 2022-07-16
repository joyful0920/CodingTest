import sys
si = sys.stdin.readline

n = int(si())
w = list(map(int, si().split()))

res = 0
results = []
def solution(results, array):
    global res
    if len(array) == 2: # 남은 구슬이 2개라면
        if sum(results) > res: # 곱들의 결과 리스트의 합이 현재의 res보다 크다면
            res = sum(results) # 해당 합으로 res 갱신
        return
    
    for i in range(1, len(array) - 1):
        temp1 = results[:] # results 복제본
        temp1.append(array[i - 1] * array[i + 1]) # 복제본에 현재 인덱스 양옆 에너지 곱 추가
        temp2 = array[:i] + array[i+1:] # 현재 인덱스 구슬을 제거한 구슬 무게 복제본
        solution(temp1, temp2) # 재귀 호출

solution(results, w)
print(res)