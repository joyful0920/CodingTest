import sys
si = sys.stdin.readline

n = int(si())

d = [[0] * 10 for _ in range(n + 1)]

# 1 자리수는 0을 제외하고(조거 : 0은 앞에 올 수 없음) 1로 초기화
for i in range(1,10):
    d[1][i] = 1

# d[n 자리 수][n자리 숫자일 때 해당 인덱스 앞에 올 수 있는 숫자]
for i in range(2, n + 1):
    for j in range(10):
        # 뒷자리가 0일 때는 앞에 1밖에 오지 못함
        if j == 0: 
            d[i][j] = d[i - 1][j + 1]
        # 뒷자리가 9일 때는 앞에 8밖에 오지 못함
        elif j == 9: 
            d[i][j] = d[i - 1][j - 1]
        # 뒷자리가 1~8일 때는 앞에 숫자가 2개씩 올 수 있음
        else:
            d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1]


print(sum(d[n]) % 1000000000)