import sys
si = sys.stdin.readline

n, k = map(int, si().split())

rank = []
for _ in range(n):
    c, g, s, b = map(int, si().split())
    rank.append((c, g, s, b)) # (국가 번호, 금메달 수, 은메달 수, 동메달 수)
    if c == k: # 국가 번호 c가 목표 국가 번호 k와 같다면
        target = (c, g, s, b) # 해당 튜플을 target에 저장

# 정렬 없이 목표 국가가 1등이라 가정하고, 완전탐색을 돌며 메달 갯수가 더 많은 국가가 등장할 때만 등수를 하나 뒤로 하는 방식도 있음!
# 람다식을 활용하여 주어진 조건에 맞게 정렬
rank.sort(key=lambda x : (-x[1], -x[2], -x[3], x[0]))

cnt = 0
for i in range(n):
    # 반례 처리: 메달 수는 동일한데 국가 번호가 다를 경우
    if rank[i][0] != k and rank[i][1] == target[1] and rank[i][2] == target[2] and rank[i][3] == target[3]:
        cnt += 1 # 카운트 변수값 1 증가
    # 국가 번호와 목표 k가 같다면
    if rank[i][0] == k:
        # 해당 인덱스 + 1에 카운트 값을 빼줌으로써 등수 출력
        print(i + 1 - cnt)
        break