import sys
si = sys.stdin.readline

# 떡의 개수와 요청한 떡의 길이 입력
n, m = list(map(int, si().split()))

# 각 떡의 개별 정보 입력
array = list(map(int, si().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡 양이 부족한 경우 더 많이 자르기
    if total < m:
        end = mid - 1
    # 떡 양이 많은 경우 덜 자르기
    else:
        result = mid
        start = mid + 1
    

print(result)