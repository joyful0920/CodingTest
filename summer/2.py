rooms = ["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"]
target = 403

def solution(rooms, target):
    temp = [[] for _ in range(10000)]
    info = dict()
    result = []

    for room in rooms:
        if room[4] == ']':
            num = int(room[1:4]) 
            temp[num] = list(map(str, room[5:].split(',')))
        elif room[5] == ']':
            num = int(room[1:5])
            temp[num] = list(map(str, room[6:].split(',')))

        if num != target:
            for people in temp[num]:
                if not people in info:
                    info[people] = [1, abs(num - target), people]
                else:
                    tmp = info[people]
                    info[people] = [tmp[0]+1, min(tmp[1], abs(num - target)), people]

    for i in info.keys():
        result.append(info[i])
    result.sort()

    answer = []
    for i in range(len(result)):
        answer.append(result[i][2])

    return answer

print(solution(rooms, target))