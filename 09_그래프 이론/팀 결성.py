import sys
si = sys.stdin.readline

# find 연산 함수
def find_parent(parent, x):
    # 루트 노드가 아니면, 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 연산 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# N, M 입력
n, m = map(int, si().split())

# 부모 테이블 생성 및 자기 자신으로 초기화
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

# 연산 입력 및 수행
for i in range(m):
    op, a, b = map(int, si().split())
    # union 연산일 경우
    if op == 0:
        union_parent(parent, a, b)
    # find 연산일 경우
    elif op == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
