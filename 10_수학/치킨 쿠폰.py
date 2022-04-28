import sys
si = sys.stdin.readline

while True:
    temp = si()
    if not temp: break
    n, k = map(int, temp.split())
    cnt = n
    s = n

    while s // k:
        cnt += s // k
        s = s // k + s % k

    print(cnt)