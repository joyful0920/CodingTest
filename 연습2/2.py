from collections import deque

arr = ["1","2","4","3","3","4","1","5"]
processes = ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]

def solution(arr, processes):
    process = deque(processes)
    length = len(processes)
    queue = deque()
    time = 0

    direct = process.popleft().split()
    for i in range(1, len(direct)):
        direct[i] = int(direct[i])
    queue.append(direct)
    queue[-1][2] = direct[1] + direct[2]
    if direct[0] == 'write':
        time += direct[1] + direct[2]

    for _ in range(1, length):
        direct = process.popleft().split()
        for i in range(1, len(direct)):
            direct[i] = int(direct[i])
        if direct[0] == 'write':
            time = queue[-1][2]
        else:
            if queue[-1][0] == 'write':
                time = queue[-1][2]
        queue.append(direct)
        if time < direct[1]:
            queue[-1][2] = direct[1] + direct[2]
        else:
            queue[-1][2] = time + direct[2]
        queue = sorted(queue, key=lambda x:x[2])
    
    while queue:
        direct = queue.popleft()
        temp = ''
        if direct[0] == 'read':
            for i in range(direct[3], direct[4] + 1):
                temp += arr[i]
        else:
            for i in range(direct[3], direct[4] + 1):
                arr[i] = direct[5]
    return queue

print(solution(arr, processes))