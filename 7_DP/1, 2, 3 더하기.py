import sys
si = sys.stdin.readline

# 테스트 케이스 수와 n 입력
t = int(si())
array = [int(si().rstrip()) for i in range(t)]

# DP 테이블 초기화
d = [float('inf')] * (11)
d[1] = 1
d[2] = 2
d[3] = 4

# 보텀업 DP
for i in range(t):
    for j in range(4, array[i] + 1):
        d[j] = d[j - 1] + d[j - 2] + d[j - 3]
    print(d[array[i]])