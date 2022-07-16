import sys
si = sys.stdin.readline

n = int(si())
s = [0] * n
w = [0] * n

for i in range(n):
    s[i], w[i] = map(int, si().split())

result = 0
def solution(idx, eggs):
    global result
    if idx == n: # 마지막 인덱스일 경우
        cnt = 0
        for i in range(n):
            if eggs[i] <= 0: # 깨진 계란 카운트
                cnt += 1
        if cnt > result: # cnt가 현재 result보다 큰 경우만 새롭게 갱신(여러 재귀함수에 대한 결과 중 최댓값 처리)
            result = cnt
        return
    
    if eggs[idx] > 0: # 현재 쥔 계란의 내구도가 남은 경우
        for i in range(n):
            flag = False
            if eggs[i] > 0 and i != idx: # 다른 계란들을 확인해서 내구도가 남았다면
                flag = True
                # 각각의 다른 계란으로 계란치기를 하기(재귀적)
                temp = eggs[:]
                temp[i] -= w[idx]
                temp[idx] -= w[i]
                solution(idx + 1, temp)
        if not flag: # 다른 계란들에 계란치기가 불가하면 다음 계란 쥐기
            solution(idx + 1, eggs)
    else: # 현재 쥔 계란으로 계란치기가 불가하면 다음 계란 쥐기
        solution(idx + 1, eggs)

solution(0, s)
print(result)