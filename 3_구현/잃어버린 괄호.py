import sys
si = sys.stdin.readline

formular = si().rstrip().split('-')
nums = []

for f in formular:
    temp = 0
    p = f.split('+')
    for e in p:
        temp += int(e)
    nums.append(temp)

result = nums[0]
for i in range(1, len(nums)):
    result -= nums[i]

print(result)