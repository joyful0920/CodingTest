import sys
si = sys.stdin.readline

# 나무의 수와 나무의 길이 입력
n, m = list(map(int, si().split()))

# 각 나무의 길이 입력
array = list(map(int, si().split()))

# 나무 자르기 함수 (이진 탐색)
def cut():
    # 이진 탐색을 위한 시작점과 끝점 설정
    start = 0
    end = max(array)
    # 이진 탐색 수행(반복적)
    result = 0
    while (start <= end):
        total = 0
        mid = (start + end) // 2
        for x in array:
            # 잘랐을 때 가져갈 수 있는 나무 길이 계산
            if x > mid:
                total += x - mid
        # 나무의 길이가 부족할 경우 더 많이 자르기
        if total < m:
            end = mid - 1
        # 나무의 길이가 더 많은 경우 덜 자르기        
        else:
            result = mid
            start = mid + 1
    return result

print(cut())