import sys
si = sys.stdin.readline

n = int(si())
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

def test(result):
    for x, y, s in result:
        if s == 0: # 기둥이라면
            # 해당 위치가 바닥 or 기둥 위 or 양옆에 보가 하나라도 있다면
            if y == 0 or [x, y - 1, 0] in result or [x - 1, y, 1] in result or [x, y, 1] in result:
                continue
            return False
        elif s == 1: # 보라면
            # 양쪽 끝 중 하나라도 밑에 기둥 or 양쪽에 보가 있다면
            if [x, y - 1, 0] in result or [x + 1, y - 1, 0] in result or ([x - 1, y, 1] in result and [x + 1, y, 1] in result):
                continue
            return False
    return True

def solution(n, build_frame):
    # 벽면으로 사용할 2차원 리스트
    array = [[(0, 0)] * (n + 1) for _ in range(n + 1)]
    result = [] # 결과를 담을 리스트

    # 설치/삭제 명령을 차례대로 수행
    for i in range(len(build_frame)):
        x, y, s, d = build_frame[i]
        if d == 1: # 설치 명령이라면
            result.append([x, y, s]) # 일단 설치
            if not test(result): # 테스트 결과가 False라면
                result.remove([x, y, s]) # 다시 삭제
        elif d == 0: # 삭제 명령이라면
            result.remove([x, y, s]) # 일단 삭제
            if not test(result): # 테스트 결과가 False라면
                result.append([x, y, s]) # 다시 설치

    result.sort() # 정렬
    return result

print(solution(n, build_frame))