import sys, bisect
si = sys.stdin.readline

t = int(si())
for _ in range(t):
    n, m = map(int, si().split())
    a = list(map(int, si().split()))
    b = sorted(list(map(int, si().split())))

    cnt = 0
    for i in a:
        cnt += (bisect.bisect(b, i - 1)) # b 중 i - 1이 들어갈 수 있는 가장 빠른 인덱스를 리턴
    print(cnt)