from itertools import combinations
import sys
si = sys.stdin.readline

n, s = map(int, si().split())
array = list(map(int, si().split()))
cnt = 0

for i in range(1, len(array) + 1):
    for each in list(combinations(array, i)):
        if sum(each) == s:
            cnt += 1

print(cnt)