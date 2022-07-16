import sys
si = sys.stdin.readline

h, w = map(int, si().split())
array = list(map(int, si().split()))
water = 0

for i in range(1, w - 1):
    left_max = max(array[:i])
    right_max = max(array[i + 1:])

    compare = min(left_max, right_max)

    if array[i] < compare:
        water += compare - array[i]

print(water)