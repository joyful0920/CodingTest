import sys
si = sys.stdin.readline

# 거스름돈 액수 입력
n = int(si())

# DP 테이블 초기화
d = [float('inf')] * 100001
d[0] = 0
d[2] = 1
d[4] = 2

# 보톰업 DP
for i in range(5, n + 1):
    d[i] = min(d[i - 5] + 1, d[i - 2] + 1)

def printD():
    if d[n] == float('inf'):
        d[n] = -1
    return d[n]

print(printD())