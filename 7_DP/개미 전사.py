import sys
si = sys.stdin.readline

# 식량 창고 갯수와 저장된 식량 갯수 입력
n = int(si().rstrip())
array = list(map(int, si().split()))

# DP 테이블 초기화
d = [0] * 101

# 보텀업 DP
d[1] = array[0]
d[2] = max(array[0], array[1])
for i in range(3, n + 1):
    d[i] = max(d[i - 1], d[i - 2] + array[i - 1])

print(d[n])