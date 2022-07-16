import sys
si = sys.stdin.readline

t = int(si())

for _ in range(t):
    commands = si().rstrip()
    vx = [0]
    vy = [0]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    now = 0
    x = 0
    y = 0
    for c in commands:
        if c == 'F':
            x += dx[now]
            y += dy[now]
            vx.append(x)
            vy.append(y)
        elif c == 'B':
            x -= dx[now]
            y -= dy[now]
            vx.append(x)
            vy.append(y)
        elif c == 'L':
            if now == 0:
                now = 3
            else:
                now -= 1
        else:
            if now == 3:
                now = 0
            else:
                now += 1
    width = abs(max(vx) - min(vx))
    height = abs(max(vy) - min(vy))
    print(width * height)