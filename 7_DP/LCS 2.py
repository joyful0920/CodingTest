import sys
si = sys.stdin.readline

s1 = [""] + list(si().rstrip())
s2 = [""] + list(si().rstrip())

dp = [[""] * len(s2) for _ in range(len(s1))]

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i - 1][j - 1] + s1[i]
        else:
            if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

result = dp[-1][-1]
print(len(result))
print(result)