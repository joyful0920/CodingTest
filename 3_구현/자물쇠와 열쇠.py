import sys
si = sys.stdin.readline

n, m = map(int, si().split())

lock = [list(map(int, si().split())) for _ in range(n)]
key = [list(map(int, si().split())) for _ in range(m)]

# 열쇠를 90도 회전시킬 함수
def rotation(array):
    n = len(array)
    m = len(array[0])
    results = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            results[i][j] = array[j][m - 1 - i]
    return results

# 자물쇠를 열 수 있는지 체크하는 함수
def check(lock):
    len_lock = len(lock) // 3
    for i in range(len_lock, len_lock * 2):
        for j in range(len_lock, len_lock * 2):
            if lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 열쇠 일부분만 맞춰 보는 작업을 용이하게 하기 위해 기존 자물쇠 정보를 담은 리스트를 3배의 길이로 연장
    extended_lock = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            extended_lock[i + n][j + n] = lock[i][j]
    
    # 열쇠를 90도씩 총 4번 돌려가며 같은 작업을 반복
    for _ in range(4):
        key = rotation(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        extended_lock[x + i][y + j] += key[i][j] # 자물쇠와 열쇠 정보 더하기
                if check(extended_lock) == True:
                    return True
                # 맞지 않는 다면 더한 값을 다시 빼주는 작업 필요
                for i in range(m):
                    for j in range(m):
                        extended_lock[x + i][y + j] -= key[i][j]
    return False

print(solution(lock, key))