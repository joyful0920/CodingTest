import sys
si = sys.stdin.readline

x = int(si())

target = 1
while x > target:
    x -= target
    target += 1

if target % 2 == 0:
    up = x
    down = target - x + 1
else:
    up = target - x + 1
    down = x

print(up, '/', down, sep='')