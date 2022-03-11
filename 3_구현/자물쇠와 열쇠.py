import sys
si = sys.stdin.readline

n, m = map(int, si().split())

lock = [list(map(int, si().split())) for _ in range(n)]
key = [list(map(int, si().split())) for _ in range(m)]

def rotation(array):
    n = len(array)
    m = len(array[0])
    results = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            results[i][j] = array[j][m - 1 - i]
    return results

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
    extended_lock = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            extended_lock[i + n][j + n] = lock[i][j]
    
    for _ in range(4):
        key = rotation(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        extended_lock[x + i][y + j] += key[i][j]
                if check(extended_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        extended_lock[x + i][y + j] -= key[i][j]
    return False

print(solution(lock, key))