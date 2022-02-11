import sys
si = sys.stdin.readline

# 정수 X 입력
x = int(si())

# DP 테이블 초기화
d = [float('inf')] * (x + 1)
d[1] = 0

# 보톰업 DP
for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수가 3으로 나뉘어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 현재의 수가 2로 나뉘어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[x])