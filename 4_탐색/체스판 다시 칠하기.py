import sys
si = sys.stdin.readline

n, m = map(int, si().split())

array = [list(map(str, str(si().rstrip()))) for _ in range(n)]
count = []

for i in range(n - 7):
    for j in range(m - 7):
        w = 0
        b = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if array[x][y] != 'W':
                        w += 1
                    if array[x][y] != 'B':
                        b += 1
                else:
                    if array[x][y] != 'B':
                        w += 1
                    if array[x][y] != 'W':
                        b += 1
        count.append(w)
        count.append(b)

print(min(count))