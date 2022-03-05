import sys
si = sys.stdin.readline

n = int(si())
array = list(map(int, si().split()))
m = int(si())
targets = list(map(int, si().split()))
array.sort()

# 이진 탐색 재귀 함수
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 1 반환
    if array[mid] == target:
        return 1
    # 중간점 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인        
    else:
        return binary_search(array, target, mid + 1, end)


for i in range(m):
    result = binary_search(array, targets[i], 0, n - 1)
    if result == None:
        print(0)
    else:
        print(result)