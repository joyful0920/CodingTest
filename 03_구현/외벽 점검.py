from itertools import permutations

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

def solution(n, weak, dist):
    # 원형의 외벽을 일직선선형으로 만들어주기
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    
    # dist 길이보다만 크게 결과값 초기화 
    result = len(dist) + 1

    for start in range(length):
        for each in list(permutations(dist, len(dist))):
            cnt = 1 # 투입할 친구 수
            # 투입한 친구가 점검 가능한 마지막 위치
            position = weak[start] + each[cnt - 1]
            # 시작점부터 모든 취약점 확인
            for i in range(start, start + length):
                # 현재 친구로는 점검이 불가능한 곳이 있다면
                if position < weak[i]:
                    cnt += 1 # 다음 친구 투입
                    if cnt > len(dist): # 투입 가능한 친구가 더는 없다면
                        break
                    position = weak[i] + each[cnt - 1]
            result = min(result, cnt) # 최솟값 갱신
    
    if result > len(dist):
        return -1
    
    return result

print(solution(n, weak, dist))