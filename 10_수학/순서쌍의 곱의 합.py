import sys
si = sys.stdin.readline

n = int(si())
nums = list(map(int, si().split()))

total = sum(nums)
result = 0

# 전체 수의 초기값에 각각의 수들을 뺀 나머지와 해당 수를 곱한 값을 결과 값에 더해가면 됨.
for i in nums:
    total -= i
    result += total * i

print(result)