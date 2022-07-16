import sys
si = sys.stdin.readline

nums = [['###', '..#', '###', '###', '#.#', '###', '###', '###', '###', '###'],
        ['#.#', '..#', '..#', '..#', '#.#', '#..', '#..', '..#', '#.#', '#.#'],
        ['#.#', '..#', '###', '###', '###', '###', '###', '..#', '###', '###'],
        ['#.#', '..#', '#..', '..#', '..#', '..#', '#.#', '..#', '#.#', '..#'],
        ['###', '..#', '###', '###', '..#', '###', '###', '..#', '###', '###']]

time = [list(map(str, si().split())) for _ in range(5)]
result = []

for i in range(4):
    temp1 = True
    for j in range(10):
        if not temp1:
            break
        temp2 = True
        for k in range(5):
            if not temp2:
                break
            for w in range(3):
                if not temp2:
                    break
                elif time[k][i][w] == '.' and k == 4 and w == 2:
                        result.append(str(j))
                        temp1 = False
                elif time[k][i][w] == '#' and time[k][i][w] == nums[k][j][w]:
                    if k == 4 and w == 2:
                        result.append(str(j))
                        temp1 = False
                elif time[k][i][w] == '#' and time[k][i][w] != nums[k][j][w]:
                    temp2 = False

print(result[0] + result[1] + ':' + result[2] + result[3])