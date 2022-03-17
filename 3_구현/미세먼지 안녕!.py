import sys
si = sys.stdin.readline

r, c, t = map(int, si().split())
array = [list(map(int, si().split())) for _ in range(r)]
copy = [[0] * c for _ in range(r)]

for i in range(r):
    if array[i][0] == -1:
        up = i
        down = i + 1
        copy[i][0] = -1

def pm(i, j):
    copy = [[0] * c for _ in range(r)]
    m = array[i][j] // 5
    rest = array[i][j]
    if 0 < i - 1:
        if copy[i - 1][j] != -1:
            copy[i - 1][j] += m
            rest -= m
    if i + 1 < r:
        if copy[i + 1][j] != -1:
            copy[i + 1][j] += m
            rest -= m
    if 0 < j - 1:
        if copy[i][j - 1] != -1:
            copy[i][j - 1] += m
            rest -= m
    if j + 1 < c:
        if copy[i][j + 1] != -1:
            copy[i][j + 1] += m
            rest -= m
    copy[i][j] += rest
    array = copy

def cleaner():
    copy = [[0] * c for _ in range(r)]
    for i in range(1, c):
        copy[0][i - 1] = array[0][i]
        copy[up][i + 1] = array[up][i]
    for i in range(1, c):
        copy[down][i + 1] = array[down][i]
        copy[r - 1][i - 1] = array[r - 1][i]
    for i in range(0, up - 1):
        copy[i + 1][0] = array[i][0]
    for i in range(0, up):
        copy[i + 1][0] = array[i][0]

    
for _ in range(t):
    for i in range(r):
        for j in range(c):
            pm(i, j)
    