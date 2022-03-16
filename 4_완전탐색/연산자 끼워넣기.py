from itertools import permutations
import sys
si = sys.stdin.readline

n = int(si())
nums = list(map(int, si().split()))
array = list(map(int, si().split()))
operators = []
results = []

for i in range(4):
    for _ in range(array[i]):
        if i == 0:
            operators.append('a')
        elif i == 1:
            operators.append('b')
        elif i == 2:
            operators.append('c')
        else:
            operators.append('d')

for i in list(set(permutations(operators, len(operators)))):
    result = nums[0]
    for j in range(len(operators)):
        if i[j] == 'a':
            result += nums[j + 1]
        elif i[j] == 'b':
            result -= nums[j + 1]
        elif i[j] == 'c':
            result *= nums[j + 1]
        else:
            if result < 0:
                result = -(abs(result) // nums[j + 1])
            else:
                result //= nums[j + 1]
    results.append(result)

print(max(results))
print(min(results))