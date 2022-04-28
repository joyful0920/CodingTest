import sys, heapq
si = sys.stdin.readline

n = int(si())
heap = []

for _ in range(n):
    x = int(si())
    if x != 0:
        heapq.heappush(heap, x)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))