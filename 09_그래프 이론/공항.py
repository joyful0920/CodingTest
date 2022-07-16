import sys
si = sys.stdin.readline

g = int(si())
p = int(si())

# 부모 테이블의 값들은 인덱스 자기 자신으로 저장
parent = [i for i in range(0, g + 1)]

# find 연산 함수
def find_parent(x):
    if parent[x] != x:
        return find_parent(parent[x])
    return x

# union 연산 함수
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

cnt = 0
for _ in range(p):
    i = int(si())
    x = find_parent(i)
    if x == 0: # 0이면 도킹 가능한 게이트가 없음을 의미
        break
    union_parent(x, x - 1) # x의 부모를 x - 1로 설정해줌으로써 도킹
    cnt += 1

print(cnt)