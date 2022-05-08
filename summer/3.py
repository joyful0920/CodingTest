line = "Q4OYPI"

def solution(line):
    querty = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']]
    left = (0, 1)
    right = (9, 1)
    answer = []

    for c in line:
        if c.isdecimal():
            if int(c) != 0:
                target = (int(c)-1, 0)
            else:
                target = (9, 0)
        else:
            if c == 'Q':
                target = (0, 1)
            elif c == 'W':
                target = (1, 1)
            elif c == 'E':
                target = (2, 1)
            elif c == 'R':
                target = (3, 1)
            elif c == 'T':
                target = (4, 1)
            elif c == 'Y':
                target = (5, 1)
            elif c == 'U':
                target = (6, 1)
            elif c == 'I':
                target = (7, 1)
            elif c == 'O':
                target = (8, 1)
            else:
                target = (9, 1)
        
        lm = abs(left[0] - target[0]) + abs(left[1] - target[1])
        rm = abs(right[0] - target[0]) + abs(right[1] - target[1])

        if lm < rm:
            answer.append(0)
            left = target
            continue
        elif lm > rm:
            answer.append(1)
            right = target
            continue
        else:
            lh = abs(left[0] - target[0])
            rh = abs(right[0] - target[0])
            if lh < rh:
                answer.append(0)
                left = target
                continue
            elif lh > rh:
                answer.append(1)
                right = target
                continue
            else:
                if 0 <= target[0] < 5:
                    answer.append(0)
                    left = target
                    continue
                else:
                    answer.append(1)
                    right = target
                    continue

    return answer

print(solution(line))