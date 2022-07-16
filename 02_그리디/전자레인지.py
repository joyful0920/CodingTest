import sys
si = sys.stdin.readline

t = int(si())
cnt = [0, 0, 0] # [3분, 1분, 10초]

# 맞출 수 없는 초(10으로 나누어 떨어지지 않는)인 경우
if t % 10 != 0:
    print(-1)
else:
    # t가 0이 될 때까지 반복
    while t != 0:
        # 남은 시간이 5분 이상인 경우
        if t >= 300:
            t -= 300
            cnt[0] += 1
        # 남은 시간이 1분 이상인 경우
        elif t >= 60:
            t -= 60
            cnt[1] += 1
        # 남은 시간이 10초 이상인 경우
        else:
            t -= 10
            cnt[2] += 1

    result = []
    for i in cnt:
        result.append(str(i))

    print(' '.join(result))