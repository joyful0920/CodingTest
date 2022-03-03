import sys
si = sys.stdin.readline

n, m = map(int, si().split())

array = list(map(int, si().split()))
total = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if array[i] + array[j] + array[k] > m:
                continue
            else:
                total = max(total, array[i] + array[j] + array[k])

print(total)