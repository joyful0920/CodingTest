import sys
from collections import deque
si = sys.stdin.readline

food_times = deque(list(map(int, si().split())))
k = int(si())

def solution(food_times, k):
    answer = 0
    time = 0
    array1 = food_times
    array2 = deque([(food_times[i], i) for i in range(len(food_times))])
    while sum(array1) != 0:
        if array1[0] != 0:
            array1[0] -= 1
            each_times, num = array2.popleft()
            array2.appendleft((each_times - 1, num))
            time += 1
        array1.rotate(-1)
        array2.rotate(-1)
        if time == k:
            break
    while array1[0] == 0:
        array1.rotate(-1)
        array2.rotate(-1)
    answer = array2[0][1] + 1
    return answer

print(solution(food_times, k))

# from collections import deque

# def solution(food_times, k):
#     answer = 0
#     time = 0
#     array1 = deque(food_times)
#     array2 = deque([(food_times[i], i) for i in range(len(food_times))])
#     while sum(array1) != 0:
#         if array1[0] != 0:
#             array1[0] -= 1
#             each_times, num = array2.popleft()
#             array2.appendleft((each_times - 1, num))
#             time += 1
#         array1.rotate(-1)
#         array2.rotate(-1)
#         if time == k:
#             break
#     while array1[0] == 0:
#         array1.rotate(-1)
#         array2.rotate(-1)
#     answer = array2[0][1] + 1
#     return answer