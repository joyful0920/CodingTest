import sys
si = sys.stdin.readline

n, c = map(int, si().split())
house = sorted([int(si()) for _ in range(n)])
result = 0

def binary_search():
    start = 1
    end = house[-1] - house[0]

    while start <= end:
        mid = (start + end) // 2
        cnt = 1
        next = house[0] + mid

        for i in range(1, len(house)):
            if next <= house[i]:
                cnt += 1
                next = house[i] + mid

        if cnt >= c:
            global result
            start = mid + 1
            result = mid
        else:
            end = mid - 1

binary_search()
print(result)