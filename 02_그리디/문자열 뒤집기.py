import sys
si = sys.stdin.readline

s = si().rstrip()
cnt = 0

for i in range(1, len(s)):
    # 0이나 1로 바뀔 때마다 카운트 +1
    if s[i] != s[i - 1]:
        cnt += 1

# 카운트수가 0이나 1일 땐 그대로 출력
if cnt == 0 or cnt == 1:
    print(cnt)
# 카운트수를 2로 나눈 나머지가 1인 경우
elif cnt % 2 == 1:
    print((cnt + 1) // 2)
# 그 외
else:
    print(cnt // 2)