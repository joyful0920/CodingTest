import sys
sys.setrecursionlimit(10**9)
si = sys.stdin.readline

nums = []
while True:
    try:
        num = int(si())
        nums.append(num)
    except:
        break

def postorder(first, end):
    if first > end:
        return
    mid = end + 1
    for i in range(first + 1, end + 1):
        if nums[first] < nums[i]:
            mid = i
            break
    
    postorder(first + 1, mid - 1)
    postorder(mid, end)
    print(nums[first])

postorder(0, len(nums) - 1)