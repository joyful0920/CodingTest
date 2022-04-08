import sys
si = sys.stdin.readline

n, k = map(int, si().split())
array = list(map(int, si().split()))

temp = 0
for i in range(k):
    temp += array[i]

result = [temp]
for i in range(1, n + 1 - k):
    temp = temp - array[i - 1] + array[i + k - 1]
    result.append(temp)

print(max(result))