import sys, heapq
si = sys.stdin.readline

n = int(si())
max_heap = []

for _ in range(n):
    x = int(si())
    if x != 0:
        heapq.heappush(max_heap, (-x, x)) # 가장 큰 값을 왼쪽에 저장할 수 있도록 (-x, x) 형태로 저장
    else:
        if len(max_heap) == 0: # 힙이 비어있으면
            print(0)
        else:
            print(heapq.heappop(max_heap)[1]) # 가장 큰(왼쪽) 값 출력