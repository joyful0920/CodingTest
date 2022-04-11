import sys
si = sys.stdin.readline

n, l = map(int, si().split())

lights = [(0, 0, 0)] # 이후 등장할 반복문에 활용하기 위해 초기 출발 지점 값 세팅
for _ in range(n):
    d, r, g = map(int, si().split())
    lights.append((d, r, g)) # (위치, 빨간불 지속시간, 초록불 지속시간)

time = 0 # 초기 경과 시간 0으로 세팅
for i in range(1, n + 1):
    d, r, g = lights[i]
    cycle = r + g # 한 사이클이 도는 데 걸리는 시간 = 빨간불 + 초록불 지속시간
    time += d - lights[i - 1][0] # 직전 신호등에서 현재 신호등까지 이동하는 데 걸리는 시간을 경과 시간에 추가
    # 현재 신호등이 빨간 불이라면 대기를 해야 하므로
    if time % cycle < r: # 현재까지 경과 시간에 해당 신호등의 사이클로 나눈 나머지 < 현재 신호등 빨간불 지속시간
        time += r - (time % cycle) # 남은 빨간불 지속시간이 대기 시간이 되므로 경과 시간에 추가

# 최종적으로 마지막 신호등에서 도로 끝까지 이동하는 데 걸리는 시간을 경과 시간에 추가
time += l - lights[-1][0]
print(time)