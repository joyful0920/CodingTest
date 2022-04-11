import sys
si = sys.stdin.readline

n, k = map(int, si().split())
array = list(map(int, si().split()))

temp = 0
# 맨 왼쪽 k개로 초기 수열합 세팅
for i in range(k):
    temp += array[i]

result = [temp] # 초기 수열합을 결과 배열에 저장
for i in range(1, n + 1 - k):
    # 수열합에서 직전 수열의 맨 왼쪽 요소는 빼주고, 현재 수열의 맨 오른쪽 요소 더하기
    temp = temp - array[i - 1] + array[i + k - 1]
    result.append(temp)

print(max(result))