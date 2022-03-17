import sys, math
si = sys.stdin.readline

n = si().rstrip()
nums = []

for i in n:
    if i != '0':
        nums.append(int(i))

for i in range(1, len(nums)):
    nums[0] = math.lcm(nums[0], nums[i])

if int(n) % nums[0] == 0:
    print(int(n))
else:
    cnt = 1
    check = False
    while True:
        for i in range(0, 10 ** cnt):
            if int(n + '0' * (cnt - len(str(i))) + str(i)) % nums[0] == 0:
                print(int(n + '0' * (cnt - len(str(i))) + str(i)))
                check = True
                break
        if check == True:
            break
        cnt += 1