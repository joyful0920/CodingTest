import sys
si = sys.stdin.readline

n = int(si())
nums = list(map(int, si().rstrip()))

print(sum(nums))