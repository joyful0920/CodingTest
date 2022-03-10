import sys
from collections import deque
si = sys.stdin.readline

n = int(si())
array = [int(si()) for _ in range(n)]

def one(array, n):
    result = round(sum(array) / n)
    return result

def two(array, n):
    temp = sorted(array)
    result = temp[n // 2]
    return result

def three(array):
    d = [0] * 8001
    queue = deque()
    for i in array:
        d[i + 4000] += 1
    cnt = max(d)
    for i in range(-4000, 4001):
        if len(queue) == 2:
            break
        elif d[i + 4000] == cnt:
            queue.append(i)
    if len(queue) == 1:
        result = queue[0]
    else:        
        result = queue[1]
    return result

def four(array, n):
    result = max(array) - min(array)
    return result

print(one(array, n))
print(two(array, n))
print(three(array))
print(four(array, n))