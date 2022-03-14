import sys
si = sys.stdin.readline

n = int(si())
clockwise = True

# 시계 방향 회전
def rotate_90(array):
    n = len(array)
    m = len(array[0])
    results = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            results[i][j] = array[j][m - 1 - i]
    return results

# 반시계 방향 회전    
def reverse_90(array):
    n = len(array)
    m = len(array[0])
    results = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            results[i][j] = array[m - 1 - j][i]
    return results

def solution(n, clockwise):
    array = [[0] * n for _ in range(n)]

    # 시계 방향인 경우
    if clockwise == True:
        for _ in range(4):
            array = rotate_90(array)
            cnt = 0
            for i in range(n // 2):
                for j in range(i, n - i - 1):
                    cnt += 1
                    array[i][j] = cnt
                if n % 2 != 0:
                    array[n // 2][n // 2] = array[n // 2 - 1][n // 2] + 1

    # 반시계 방향인 경우
    else:
        for _ in range(4):
            array = reverse_90(array)
            cnt = 0
            for i in range(n // 2):
                for j in range(-i - 1, i - n, -1):
                    cnt += 1
                    array[i][j] = cnt
                if n % 2 != 0:
                    array[n // 2][n // 2] = array[n // 2 - 1][n // 2] + 1
        
    return array

print(solution(n, clockwise))