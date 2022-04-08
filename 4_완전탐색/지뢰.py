import sys
si = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(si())
mines = [int(si()) for _ in range(n)]
exploded = [False] * n
result = []

def explode(index):
    if index - 1 >= 0 and exploded[index - 1] == False:
        if mines[index] > mines[index - 1]:
            exploded[index - 1] = True
            explode(index - 1)
    if index + 1 <= n - 1 and exploded[index + 1] == False:
        if mines[index] > mines[index + 1]:
            exploded[index + 1] = True
            explode(index + 1)

if n == 1:
    print(1)
else:
    for i in range(n):
        if i == 0:
            if mines[i] >= mines[i + 1] and exploded[i] == False:
                exploded[i] == True
                result.append(i + 1)
                explode(i)
        elif i == n - 1:
            if mines[i] >= mines[i - 1] and exploded[i] == False:
                exploded[i] == True
                result.append(i + 1)
                explode(i)
        else:
            if mines[i - 1] <= mines[i] >= mines[i + 1] and exploded[i] == False:
                exploded[i] == True
                result.append(i + 1)
                explode(i)

    result.sort()

    for i in result:
        print(i)