import sys
si = sys.stdin.readline

king, rock, n = map(str, si().rstrip().split())
move_king = [si().rstrip() for _ in range(int(n))]

def change(x):
    if x == 'A':
        return 1
    elif x == 'B':
        return 2
    elif x == 'C':
        return 3
    elif x == 'D':
        return 4
    elif x == 'E':
        return 5
    elif x == 'F':
        return 6
    elif x == 'G':
        return 7
    else:
        return 8

def reverse(x):
    if x == 1:
        return 'A'
    elif x == 2:
        return 'B'
    elif x == 3:
        return 'C'
    elif x == 4:
        return 'D'
    elif x == 5:
        return 'E'
    elif x == 6:
        return 'F'
    elif x == 7:
        return 'G'
    else:
        return 'H'
        
king_x = change(king[0])
king_y = int(king[1])
rock_x = change(rock[0])
rock_y = int(rock[1])

for i in move_king:
    if i == 'R':
        if king_x == 8:
            continue
        elif (king_x + 1, king_y) == (rock_x, rock_y):
            if rock_x == 8:
                continue
            else:
                king_x += 1
                rock_x += 1
        else:
            king_x += 1
    elif i == 'L':
        if king_x == 1:
            continue
        elif (king_x - 1, king_y) == (rock_x, rock_y):
            if rock_x == 1:
                continue
            else:
                king_x -= 1
                rock_x -= 1
        else:
            king_x -= 1
    elif i == 'B':
        if king_y == 1:
            continue
        elif (king_x, king_y - 1) == (rock_x, rock_y):
            if rock_y == 1:
                continue
            else:
                king_y -= 1
                rock_y -= 1
        else:
            king_y -= 1
    elif i == 'T':
        if king_y == 8:
            continue
        elif (king_x, king_y + 1) == (rock_x, rock_y):
            if rock_y == 8:
                continue
            else:
                king_y += 1
                rock_y += 1
        else:
            king_y += 1    
    elif i == 'RT':
        if king_x == 8 or king_y == 8:
            continue
        elif (king_x + 1, king_y + 1) == (rock_x, rock_y):
            if rock_x == 8 or rock_y == 8:
                continue
            else:
                king_x += 1
                king_y += 1
                rock_x += 1
                rock_y += 1
        else:
            king_x += 1
            king_y += 1        
    elif i == 'LT':
        if king_x == 1 or king_y == 8:
            continue
        elif (king_x - 1, king_y + 1) == (rock_x, rock_y):
            if rock_x == 1 or rock_y == 8:
                continue
            else:
                king_x -= 1
                king_y += 1
                rock_x -= 1
                rock_y += 1
        else:
            king_x -= 1
            king_y += 1
    elif i == 'RB':
        if king_x == 8 or king_y == 1:
            continue
        elif (king_x + 1, king_y - 1) == (rock_x, rock_y):
            if rock_x == 8 or rock_y == 1:
                continue
            else:
                king_x += 1
                king_y -= 1
                rock_x += 1
                rock_y -= 1
        else:
            king_x += 1
            king_y -= 1
    else:
        if king_x == 1 or king_y == 1:
            continue
        elif (king_x - 1, king_y - 1) == (rock_x, rock_y):
            if rock_x == 1 or rock_y == 1:
                continue
            else:
                king_x -= 1
                king_y -= 1
                rock_x -= 1
                rock_y -= 1
        else:
            king_x -= 1
            king_y -= 1

king_x = reverse(king_x)
rock_x = reverse(rock_x)

print(king_x + str(king_y))
print(rock_x + str(rock_y))