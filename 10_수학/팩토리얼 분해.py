import sys
si = sys.stdin.readline

n = int(si())
f = 2432902008176640000

# n이 0이라면 팩토리얼 합으로 표현불가
if n == 0:
    print('NO')
    exit()

# 주어진 n보다 작은 팩토리얼 값중 가장 큰 값부터 빼주며 확인
# n이 최대 1,000,000,000,000,000,000이므로 19!부터 빼주면 됨
for i in range(20, 0, -1):
    f //= i
    # 현재 n이 현재 팩토리얼 값 f보다 클 경우 빼주기
    if n >= f:
        n -= f

# n을 0으로 만들 수 있는 경우만 YES 출력
if n == 0:
    print('YES')
else:
    print('NO')