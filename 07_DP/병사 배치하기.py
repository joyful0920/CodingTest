import sys
si = sys.stdin.readline

n = int(si())
soldiers = list(map(int, si().split()))
dp = [1] * n

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if soldiers[i] > soldiers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))