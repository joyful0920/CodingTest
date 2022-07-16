import sys
si = sys.stdin.readline

n = int(si())
paper = [list(map(int, si().split())) for _ in range(n)]
white = 0
blue = 0

def devide(x, y, size):
    global white
    global blue
    standard = paper[x][y]
    if size == 1:
        if standard == 0:
            white += 1
        else:
            blue += 1
    else:
        for i in range(x, x + size):
            for j in range(y, y + size):
                if paper[i][j] != standard:
                    size //= 2
                    devide(x, y, size)
                    devide(x, y + size, size)
                    devide(x + size, y, size)
                    devide(x + size, y + size, size)
                    return
                if i == x + size - 1 and j == y + size - 1:
                    if standard == 0:
                        white += 1
                    else:
                        blue += 1

devide(0, 0, n)
print(white)
print(blue)