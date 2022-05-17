import sys
si = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

while True:
    m, n = map(int, si().split())
    if m == 0 and n == 0:
        exit(0)

    parent = [0] * (n + 1) 
    for i in range(1, n + 1):
        parent[i] = i

    edges = []
    total = 0
    for _ in range(n):
        a, b, cost = map(int, si().split())
        total += cost
        edges.append((cost, a, b))
    edges.sort()

    temp = 0
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            temp += cost

    print(total - temp)