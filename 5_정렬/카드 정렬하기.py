import sys, heapq
si = sys.stdin.readline

n = int(si())
bundle = []

for _ in range(n):
    heapq.heappush(bundle, int(si()))

result = 0

while len(bundle) != 1:
    temp = heapq.heappop(bundle) + heapq.heappop(bundle)
    result += temp
    heapq.heappush(bundle, temp)

print(result)