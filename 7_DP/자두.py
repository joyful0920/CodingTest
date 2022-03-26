import sys
si = sys.stdin.readline

t, w = map(int, si().split())
plums = [0] + [int(si()) for _ in range(t)]

d = [[0] * (w + 1) for _ in range(t + 1)]

for i in range(1, t + 1):
    if plums[i] == 1:
        d[i][0] = d[i - 1][0] + 1
    else:
        d[i][0] = d[i - 1][0]
    
    for j in range(1, w + 1):
        if j > i:
            break

        if plums[i] == 1 and j % 2 == 0:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - 1]) + 1
        elif plums[i] == 2 and j % 2 == 1:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - 1]) + 1
        else:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - 1])

print(max(d[-1]))