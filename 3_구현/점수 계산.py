import sys
si = sys.stdin.readline

n = int(si())
array = list(map(int, si().split()))
point = 0
result = 0

for i in array:
    if i == 1:
        point += 1
        result += point
    else:
        point = 0

print(result)