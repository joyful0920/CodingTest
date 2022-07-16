import sys
si = sys.stdin.readline

k, n = map(int, si().split())
array = [int(si()) for _ in range(k)]

start = 1
end = max(array)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in array:
        cnt += i // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)