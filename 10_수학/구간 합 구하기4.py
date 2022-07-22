import sys

si = sys.stdin.readline

n, m = map(int, si().split())
numbers = list(map(int, si().split()))

results = [0]
for i in range(len(numbers)):
    results.append(results[i] + numbers[i])

for _ in range(m):
    start, end = map(int, si().split())
    result = results[end] - results[start - 1]
    print(result)
