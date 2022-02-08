import sys
si = sys.stdin.readline

# 화폐 개수 및 만들고자 하는 가치 입력
n, m = map(int, si().split())

# 화폐 가치 입력
array = list(int(si().rstrip()) for _ in range(n))

# DP 테이블 초기화
d = [10001] * (m + 1) # 초기엔 모두 불가능(10001)로 초기화
d[0] = 0 # 0원이 목표일 땐 경우의 수 0

# 보톰업 DP
for i in range(n):
    for j in range(array[i], m + 1):
        d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])