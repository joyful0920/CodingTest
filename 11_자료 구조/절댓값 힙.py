import sys, heapq
si = sys.stdin.readline

n = int(si())
q = []

for _ in range(n):
    x = int(si())
    if x != 0:
        heapq.heappush(q, (abs(x), x))
    else:
        if len(q) != 0:
            print(q[0][1])
            heapq.heappop(q)[0]
        else:
            print(0)
