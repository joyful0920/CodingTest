import sys
si = sys.stdin.readline

nums = list(si().rstrip())
l = len(nums)

d = [0] * (l + 1)
d[0] = 1

if nums[0] == "0":
    d[1] = 0
else:
    d[1] = 1

for i in range(2, l + 1):
    if 0 < int(nums[i - 1]):
        d[i] = d[i - 1]
    if 10 <= int(nums[i - 2] + nums[i - 1]) <= 26:
        d[i] += d[i - 2]

print(d[l] % 1000000)