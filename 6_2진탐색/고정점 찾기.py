import sys
si = sys.stdin.readline

n = int(si())
array = list(map(int, si().split()))

def fixed_point():
    start = 0
    end = n - 1
    while (start <= end):
        mid = (start + end) // 2
        # 중간 인덱스 지점의 값이 인덱스보다 클 경우
        if array[mid] > mid:
            end = mid - 1
        # 중간 인덱스 지점의 값이 인덱스보다 작을 경우
        elif array[mid] < mid:
            start = mid + 1
        # 중간 인덱스 지점의 값과 인덱스가 일치할 경우
        else:
            return mid
    return - 1

print(fixed_point())