import sys
si = sys.stdin.readline

n = int(si())
m = int(si())

graph = [list(map(int, si().split())) for _ in range(n)]
plan = list(map(int, si().split()))

# find 연산 함수
def find_parent(parent, x):
    if parent[x] != x: # 루트 노드가 아닐 경우
        return find_parent(parent, parent[x]) # 해당 노드의 루트를 재귀적으로 찾기
    return x # 루트 노드 리턴

# union 연산 함수
def union_parent(parent, a, b):
    # 두 노드의 루트 노드를 찾기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 보다 작은 노드를 보다 큰 노드의 부모 노드로 설정
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * n
for i in range(n):
    parent[i] = i # 부모 테이블의 부모를 자기 자신으로 초기화

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: # 연결된 노드라면
            union_parent(parent, i, j) # union 연산으로 루트 노드 통일

# 주어진 여행 계획 검사
result = True
temp = find_parent(parent, plan[0] - 1)
for i in plan:
    # 두 도시의 루트가 다르다면
    if temp != find_parent(parent, i - 1):
        result = False
        break

if result:
    print("YES")
else:
    print("NO")