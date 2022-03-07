import sys
si = sys.stdin.readline

s = si().rstrip()
cnt = 0

for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        cnt += 1

if cnt == 0 or cnt == 1:
    print(cnt)
elif cnt % 2 == 1:
    print((cnt + 1) // 2)
else:
    print(cnt // 2)