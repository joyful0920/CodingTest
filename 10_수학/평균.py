import sys
si = sys.stdin.readline

n = int(si())

array = list(map(int, si().split()))

def cal():
    max_point = max(array)
    for i in range(n):
        array[i] = array[i] / max_point * 100
    result = sum(array) / n
    return result

print(cal())