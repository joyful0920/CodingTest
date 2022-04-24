import sys
si = sys.stdin.readline

n, m, b = map(int, si().split())
array = [list(map(int, si().split())) for _ in range(n)]

result_time = float('inf')
height = 0

# 땅고르기
def minecraft(standard):
    blocks = 0
    need = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] > standard: # 현재 기준이 되는 목표값보다 높은 땅인 경우
                blocks += array[i][j] - standard # 초과되는 블록갯수를 보유 블록갯수에 추가
            else: # 낮은 땅인 경우
                need += standard - array[i][j] # 필요로 하는 블록 갯수에 추가
    return need, blocks

for h in range(257):
    need, blocks = minecraft(h)
    inventory = b + blocks # 기존 보유 블록 갯수에 땅고르기 후 얻은 블록 갯수 추가
    if need > inventory: # 필요한 블록 갯수가 부족할 경우
        continue
    # 부족하지 않다면 땅고르기에 들은 시간 계산
    time = 2 * blocks + need
    if time <= result_time: # 최소 시간으로 업데이트
        result_time = time
        height = h

print(result_time, height)