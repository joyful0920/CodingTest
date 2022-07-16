import sys
si = sys.stdin.readline

formula = si().rstrip()
m = [[0, 0, 0] for _ in range(3)]

i = 0
for f in formula:
    if f == 'C':
        j = 0
        m[i][j] += 1
    elif f == 'H':
        j = 1
        m[i][j] += 1
    elif f == 'O':
        j = 2
        m[i][j] += 1
    elif f == '+' or f == '=':
        i += 1
    else: # 숫자가 오는 경우 해당 숫자만큼 더해야 함(직전에 1을 더해줬으므로 -1해서)
        m[i][j] += int(f) - 1

for i in range(1, 11):
    for j in range(1, 11):
        for k in range(1, 11):
            for x in range(3):
                if m[0][x] * i + m[1][x] * j != m[2][x] * k:
                    break
                else:
                    if x == 2:
                        print(i, j, k)
                        exit(0)