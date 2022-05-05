import itertools

from itertools import combinations
import sys
si = sys.stdin.readline

words = si().rstrip()
nums = [i for i in range(1, len(words))]

result = []
for picked in sorted(list(combinations(nums, 2))):
    a = words[:picked[0]]
    b = words[picked[0]:picked[1]]
    c = words[picked[1]:]
    result.append(a[::-1] + b[::-1] + c[::-1])

result.sort()
print(result[0])