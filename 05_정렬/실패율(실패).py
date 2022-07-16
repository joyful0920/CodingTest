N = 4
stages = [4,4,4,4,4]

def solution(N, stages):
    status = [[0, 0, 0, 0] for _ in range(N + 1)]
    for i in range(1, N + 1):
        status[i][0] = i
    stages = sorted(stages)

    for i in stages:
        if i == N + 1:
            for j in range(1, N + 1):
                status[j][3] += 1
        else:
            status[i][2] += 1
            for j in range(i, 0, -1):
                status[j][3] += 1

    for i in range(1, N + 1):
        status[i][1] = status[i][2] / status[i][3]

    status.pop(0)    
    status.sort(key=lambda x : -x[1])

    fail = []
    for i in status:
        fail.append(i[0])

    return fail

print(solution(N, stages))