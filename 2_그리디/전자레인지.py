import sys
si = sys.stdin.readline

t = int(si())
cnt = [0, 0, 0]

if t % 10 != 0:
    print(-1)
else:
    while t != 0:
        if t >= 300:
            t -= 300
            cnt[0] += 1
        elif t >= 60:
            t -= 60
            cnt[1] += 1
        else:
            t -= 10
            cnt[2] += 1

    result = []
    for i in cnt:
        result.append(str(i))

    print(' '.join(result))