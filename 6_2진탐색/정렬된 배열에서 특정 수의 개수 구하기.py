from bisect import bisect_left, bisect_right
import sys
si = sys.stdin.readline

n, x = map(int, si().split())
a = list(map(int, si().split()))

def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)

    if right_index - left_index != 0:
        return right_index - left_index
    else:
        return -1

print(count_by_range(a, x, x))