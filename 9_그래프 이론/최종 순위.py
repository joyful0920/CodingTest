from collections import deque
import sys
si = sys.stdin.readline

t = int(si())

for _ in range(t):
    n = int(si())
    indegree = [0] * (n + 1)
    graph = [[False] * (n + 1) for _ in range(n + 1)]

    last_year = list(map(int, si().split()))
    for i in range(n):
        for j in range(i + 1, n):
            # 2차원 리스트 값을 True로 바꿔줌으로써
            # 해당 행을 인덱스로 하는 팀이 해당 열을 인덱스로 하는 팀보다 앞순위임을 명시
            graph[last_year[i]][last_year[j]] = True
            indegree[last_year[j]] += 1 # 차수 + 1
    
    m = int(si())
    for i in range(m): # 순위 뒤바꾸기
        a, b = map(int, si().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1
    
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    
    only = True
    cycle = False

    for _ in range(n):
        if len(q) == 0: # n번 반복이 돌기 전에 q가 빈다면 사이클 발생을 의미
            cycle = True
            break
        if len(q) >= 2: # 같은 순간에 q의 길이가 2 이상이 되면 순위 특정 불가
            only = False
            break
        now = q.popleft()
        result.append(now)
        for i in range(1, n + 1):
            if graph[now][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
    
    if cycle:
        print("IMPOSSIBLE")
    elif not only:
        print('?')
    else:
        print(*result)