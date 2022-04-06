import sys
si = sys.stdin.readline

n, l = map(int, si().split())

lights = [(0, 0, 0)]
for _ in range(n):
    d, r, g = map(int, si().split())
    lights.append((d, r, g))

time = 0
for i in range(1, n + 1):
    d, r, g = lights[i]
    cycle = r + g
    time += d - lights[i - 1][0]
    if time % cycle < r:
        time += r - (time % cycle) 

time += l - lights[-1][0]
print(time)