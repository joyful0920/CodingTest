import sys
si = sys.stdin.readline

n = int(si())
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

def solution(n, build_frame):
    # 벽면으로 사용할 2차원 리스트
    array = [[(0, 0)] * (n + 1) for _ in range(n + 1)]
    result = [] # 결과를 담을 리스트

    # 설치/삭제 명령을 차례대로 수행
    for i in range(len(build_frame)):
        x, y, s, d = build_frame[i]
        if d == 1: # 설치 명령이라면
            if s == 0: # 기둥을 설치해야 한다면
                # 해당 위치가 바닥 또는 기둥이나 보가 있다면
                if y == 0 or array[y - 1][x][0] == 1 or array[y][x - 1][1] == 1 or array[y][x][1] == 1:
                    # 해당 위치에서 위로 기둥 설치
                    b = array[y][x][1]
                    array[y][x]= (1, b)
                    # 결과물에 추가
                    result.append([x, y, s])
            elif s == 1: # 보를 설치해야 한다면
                # 해당 위치에 기둥이나 그 오른쪽에 기둥 or 양쪽에 보가 있다면
                if (array[y - 1][x][0] == 1 or array[y - 1][x + 1][0] == 1) or (array[y][x - 1][1] == 1 and array[y][x + 1][1] == 1):
                    # 해당 위치에서 오른쪽으로 보 설치
                    g = array[y][x][0]
                    array[y][x] = (g, 1)
                    # 결과물에 추가
                    result.append([x, y, s])
        elif d == 0: # 삭제 명령이라면
            if s == 0: # 기둥을 삭제해야 한다면
                # 해당 위치에서 위로 설치된 기둥이 존재한다면
                if array[y][x][0] == 1:
                    b = array[y][x][1]
                    array[y][x] = (0, b) # 삭제
                    result.remove([x, y, s]) # 결과물에서도 삭제
            elif s == 1: # 보를 삭제해야 한다면
                # 해당 위치에서 오른쪽으로 보가 존재한다면
                if array[y][x][1] == 1:
                    g = array[y][x][0]
                    array[y][x] = (g, 0) # 삭제
                    result.remove([x, y, s]) # 결과물에서도 삭제

    result.sort()
    return result

print(solution(n, build_frame))