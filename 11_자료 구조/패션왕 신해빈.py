from collections import Counter
import sys
si = sys.stdin.readline

t = int(si())

for _ in range(t):
    n = int(si())
    array = []
    for _ in range(n):
        cloth, category = map(str, si().rstrip().split())
        array.append(category)
    result = Counter(array)
    num = 1
    for i in result:
        num *= result[i] + 1
    print(num - 1)