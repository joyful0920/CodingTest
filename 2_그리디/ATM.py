import sys
si = sys.stdin.readline

n = int(si())
times = sorted(list(map(int, si().split()))) # 인출에 걸리는 시간을 오름차순 정렬

result = 0
# 각각의 사람들이 돈을 인출하는 데 걸리는 총 시간 구하기
for i in range(1, n + 1):
    for j in range(i): # 각각 사람의 바로 앞 사람의 인출시간을 누적해가며
        result += times[j]

print(result)