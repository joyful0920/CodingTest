import sys
si = sys.stdin.readline

# 정수 X 입력
x = int(si())

# DP 테이블 초기화
d = [0] * 30001 # [float('inf')] * (n + 1)

# 보톰업 DP
for i in range(2, x + 1): # 2 ~ x
    # 현재의 수에서 1을 뺴는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수가 2로 나뉘어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[int(i / 2)] + 1)
    # 현재의 수가 3으로 나뉘어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[int(i / 3)] + 1)
    # 현재의 수가 5로 나뉘어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[int(i / 5)] + 1)
    
    # d[1] = 0, d[2], d[3], d[4], ... d[x]

print(d[x])