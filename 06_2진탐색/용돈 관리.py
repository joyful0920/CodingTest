import sys
si = sys.stdin.readline

# 용돈을 사용할 일수와 인출횟수 입력
n, m = map(int, si().split())

# 날짜 순서대로 필요한 용돈 입력
array = list(int(si().rstrip()) for _ in range(n))

def calc():
    # 이진 탐색을 위한 시작점과 끝점 설정
    start = max(array)
    end = sum(array)
    k = 0 # K값 초기화

    # 이진 탐색 수행(반복적)
    while (start <= end):
        mid = (start + end) // 2
        left = mid # 잔여 용돈 초기화
        cnt = 1 # 인출횟수 리셋

        # 용돈 인출이 새로 필요한지 계산
        for i in range(n):
            if left < array[i]:
                left = mid
                cnt += 1 # 필요 하에 인출하면 횟수 카운트
            left -= array[i]

        # 인출횟수가 m번보다 많으면 더 많은 금액을 매번 인출도록
        if cnt > m:
            start = mid + 1
        # 인출횟수가 m번보다 적거나 같으면
        else:
            k = mid
            end = mid - 1

    return k

print(calc())