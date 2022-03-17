import sys
si = sys.stdin.readline

n = int(si()) # N 입력
array = list(map(int, si().split())) # N개의 정수
m = int(si()) # M 입력
targets = list(map(int, si().split())) # M개의 수들
array.sort() # 탐색을 용이하게 하기 위해 오름차순 정렬

# 이진 탐색 함수 (재귀)
def binary_search(array, target, start, end):
    # 시작점이 끝점보다 클 경우엔 None을 반환하며 재귀함수 종료
    if start > end:
        return None
    mid = (start + end) // 2 # 중간 지점 인덱스 계산
    # 찾은 경우 1 반환
    if array[mid] == target:
        return 1
    # 중간점 값보다 찾고자 하는 값이 작은 경우 왼쪽 절반을 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점 값보다 찾고자 하는 값이 큰 경우 오른쪽 절반을 확인        
    else:
        return binary_search(array, target, mid + 1, end)

# M개의 수들에 대해 이진 탐색 수행
for i in range(m):
    result = binary_search(array, targets[i], 0, n - 1)
    if result == None: # array 안에 존재하지 않는 수라면
        print(0)
    else:
        print(result)