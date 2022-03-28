import sys
si = sys.stdin.readline

# 구입하고자 하는 카드개수 n 입력
n = int(si())

# 카드팩 가격 입력
# 1번 인덱스부터 사용하기 위해 
p = [0] + list(map(int, si().split()))

# DP 테이블 -> 카드 갯수에 따른 지불 최댓값을 저장
d = [0] * (n + 1) # 인덱스의 범위 : 1 ~ n

# 보톰업 DP : 이중 반복문 사용
# D[1]부터 차례대로 구해 최종적으로 D[n] 구하기
for i in range(1, n + 1): # 1 ~ n
    for j in range(1, i + 1): # 1 ~ i
        d[i] = max(d[i], d[i - j] + p[j])
        
print(d[n])