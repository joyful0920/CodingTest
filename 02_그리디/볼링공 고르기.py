import sys
si = sys.stdin.readline

n, m = map(int, si().split())
array = list(map(int, si().split()))
d = [0] * 11
result = 0

# 무게 별 공 개수 초기화
for i in array:
    d[i] += 1

for i in range(1, m + 1):
    n -= d[i] # 무게가 i인 볼링공 갯수 제외
    result += d[i] * n # 현재 선택한 i 공 갯수와 그 나머지 경우의 수를 곱한 값을 결과값에 더하기

print(result)