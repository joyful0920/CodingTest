import sys
si = sys.stdin.readline

n, m = map(int, si().split())
nums = list(map(int, si().split()))

left, right = 0, 1
cnt = 0

while left <= right and right <= n:
    temp = nums[left:right]
    total = sum(temp)

    if total < m: # 합이 m보다 작을 경우
        right += 1 # 오른쪽 포인터 이동
    elif total > m: # 클 경우
        left += 1 # 왼쪽 포인터 이동
    else: # 같을 경우
        cnt += 1
        right += 1 # 오른쪽 포인터 이동

print(cnt)