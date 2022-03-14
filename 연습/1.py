import sys
si = sys.stdin.readline
INF = float('inf')

coins = [1, 5, 10, 50, 100, 500]
costs = [2, 11, 20, 100, 200, 600]
money = int(si())

d = [INF] * (money + 1)
d[0] = 0

for i in range(6):
    for j in range(coins[i], money + 1):
        d[j] = min(d[j], d[j - coins[i]] + costs[i])

print(d[money])