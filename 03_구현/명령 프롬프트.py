import sys
si = sys.stdin.readline

n = int(si())
files = [list(map(str, si().rstrip())) for _ in range(n)]
result = files[0]

for i in range(1, n):
    for j in range(len(files[i])):
        if files[0][j] != files[i][j]:
            result[j] = '?'

print(''.join(result))