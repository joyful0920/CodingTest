import sys
si = sys.stdin.readline

n = int(si())
nums = list(map(int, si().split()))

up = [1] * n
down = [1] * n

for i in range(1, n):
    if nums[i] >= nums[i - 1]:
        up[i] = max(up[i], up[i - 1] + 1)
    if nums[i] <= nums[i - 1]:
        down[i] = max(down[i], down[i - 1] + 1)

print(max(max(up), max(down)))