import sys
si = sys.stdin.readline

t = int(si())

def people(i, j):
    for num in range(1, j + 1):
        d[i][j] += d[i - 1][num]
    return d[i][j]

for _ in range(t):
    # k, n 입력
    k = int(si())
    n = int(si())
    # 거주 인원을 저장할 DP 테이블
    d = [[0] * (n + 1) for _ in range(k + 1)]
    # 0층 DP 테이블 초기화
    for i in range(1, n + 1):
        d[0][i] = i
    # 보톰업 DP
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            d[i][j] = people(i, j)
    # k층 n호 거주인원 출력
    print(d[k][n])