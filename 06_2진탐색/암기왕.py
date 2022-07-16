import sys
si = sys.stdin.readline

def binary_search(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start  = mid + 1
    return 0

t = int(si())

for _ in range(t):
    n = int(si())
    memo1 = sorted(list(map(int, si().split())))
    m = int(si())
    memo2 = list(map(int, si().split()))
    for num in memo2:
        print(binary_search(memo1, 0, n - 1, num))