from itertools import combinations
import sys
si = sys.stdin.readline

n, m = map(int, si().split())
nums = [i for i in range(1, n + 1)]

for each in list(combinations(nums, m)):
    print(*each)