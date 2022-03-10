import sys
si = sys.stdin.readline

n, m, b = map(int, si().split())

array = [list(map(int, si().split())) for _ in range(n)]

result_time = float('inf')
height = 0

def rumbling(standard):
    blocks = 0
    need = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] > standard:
                blocks += array[i][j] - standard
            else:
                need += standard - array[i][j]
    return need, blocks

for h in range(257):
    need, blocks = rumbling(h)
    inventory = blocks + b                
    if need > inventory:
        continue
    time = 2 * blocks + need
    if time <= result_time:
        result_time = time
        height = h

print(result_time, height)