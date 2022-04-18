import sys
si = sys.stdin.readline

t = int(si())

for _ in range(t):
    n, m = map(int, si().split())
    mines = list(map(int, si().split()))
    d = [0] * (n * m)
    
    for i in range(m):
        for j in range(n):
            x = i + j * m
            for k in range(-1, 2):
                bx = x - 1 - (k * m)
                if 0 <= bx < n * m:
                    d[x] = max(d[x], d[bx] + mines[x])
                else:
                    d[x] = max(d[x], mines[x])

    print(max(d))