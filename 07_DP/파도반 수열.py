import sys
si = sys.stdin.readline

# 테스트 케이스 개수 입력
t = int(si())

# 나선에 있는 변 길이를 저장할 DP 테이블
d = [0] * 101
d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 2
d[5] = 2

# 보톰업 DP
for i in range(6, 101):
    d[i] = d[i - 1] + d[i - 5]

# N 입력 및 P(N)출력
for i in range(t):
    n = int(si())
    print(d[n])