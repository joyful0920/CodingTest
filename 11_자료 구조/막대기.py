import sys
from collections import deque
si = sys.stdin.readline

n = int(si())
array = deque([int(si().rstrip()) for _ in range(n)])
cnt = 1
max_length = array.pop()

while len(array) != 0:
    right_bar = array.pop()
    if right_bar > max_length:
        cnt += 1
        max_length = right_bar

print(cnt)