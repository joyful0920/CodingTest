import sys
si = sys.stdin.readline

n, m = map(int, si().split())
array = list(map(int, si().split()))

start = max(array) # 가장 긴 강의 길이
end = sum(array) # 전체 강의 길이

result = end
while start <= end:
    mid = (start + end) // 2
    temp = 0
    cnt = 1

    for i in range(n):
        temp += array[i]
        # 블루레이 하나의 길이를 넘는다면
        if temp > mid:
            cnt += 1
            temp = array[i]

    # 필요한 블루레이 갯수가 주어진 갯수보다 큰 경우
    if cnt > m:
        start = mid + 1 # 블루레이 길이를 더 길게
    else:
        result = mid # 결과값을 현재 mid로 갱신
        end = mid - 1 # 블루레이 길이를 더 짧게 하여 최단 길이 찾기

print(result)