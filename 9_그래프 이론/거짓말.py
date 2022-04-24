import sys
si = sys.stdin.readline

n, m = map(int, si().split())
truth = list(map(int, si().split()))[1:]

parties = []
parent = list(range(n + 1))

# find 연산 함수
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# union 연산 함수
def union(parent, a, b, truth):
    a = find(parent, a)
    b = find(parent, b)

    # 두 사람 다 진실을 알고 있다면 연산 즉시종료
    if a in truth and b in truth:
        return
    # 한 사람만 아는 경우 해당 사람을 모르는 사람의 부모로
    if a in truth:
        parent[b] = a
    elif b in truth:
        parent[a] = b
    # 둘 다 모르는 경우는 더 작은 쪽을 부모로 (한 파티로 묶기 위해서 필요)
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

for _ in range(m):
    party_info = list(map(int, si().split()))
    party_len = party_info[0]
    party = party_info[1:]

    # 파티 내 모든 요소를 돌며 union 연산 수행
    for i in range(party_len - 1):
        union(parent, party[i], party[i + 1], truth)

    parties.append(party)

cnt = 0
for party in parties:
    temp = True
    for i in range(len(party)):
        # 부모가 진실을 알고 있는 사람이라면
        if find(parent, party[i]) in truth:
            temp = False
            break
    if temp:
        cnt += 1

print(cnt)