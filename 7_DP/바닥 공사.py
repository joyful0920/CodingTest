import sys
si = sys.stdin.readline

# 가로 길이 N 입력
n = int(si())

# DP 테이블 초기화
d = [0] * 1001

# 보텀업 DP
d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = (d[i - 1] + d[i - 2] * 2) % 796796

print(d[n])