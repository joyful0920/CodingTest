from itertools import combinations
from copy import deepcopy
import sys
si = sys.stdin.readline

# 복도 정보 입력
n = int(si())
graph = [list(map(str, si().split())) for _ in range(n)]

# 장애물 설치가 가능한 위치와 교사의 위치 튜플 각각 리스트에 저장
obstacles = []
teachers = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'X':
            obstacles.append((i, j))
        elif graph[i][j] == 'T':
            teachers.append((i, j))

# 감시를 수행할 함수
def watch_x(x, y, end, step, graph):
    for i in range(x, end, step):
        if graph[i][y] == 'O':
            return True
        elif graph[i][y] == 'S':
            return False
    return True # 장애물 또는 학생 모두 없는 경우

def watch_y(x, y, end, step, graph):
    for i in range(y, end, step):
        if graph[x][i] == 'O':
            return True
        elif graph[x][i] == 'S':
            return False
    return True

# 장애물을 설치할 모든 조합을 구하고 각각 경우마다 반복
for picked in list(combinations(obstacles, 3)):
    cnt = 0
    # 일단 graph의 카피본을 떠놓고
    graph_copy = deepcopy(graph)
    # 뽑은 세 곳에 장애물 설치
    for each_picked in picked:
        x, y = each_picked
        graph_copy[x][y] = 'O'
    # 교사들이 각각 감시 수행
    for teacher in teachers:
        x, y = teacher
        # 상 방향 감시
        if watch_x(x - 1, y, -1, -1, graph_copy) == True:
            # 하 방향 감시
            if watch_x(x + 1, y, n, 1, graph_copy) == True:
                # 좌 방향 감시
                if watch_y(x, y - 1, -1, -1, graph_copy) == True:
                    # 우 방향 감시
                    if watch_y(x, y + 1, n, 1, graph_copy) == True:
                        cnt += 1
    # 카운트값이 선생님 수와 일치한다면 모든 선생님의 감시를 피할 수 있다는 것
    if cnt == len(teachers):
        break

if cnt == len(teachers):
    print('YES')
else:
    print('NO')