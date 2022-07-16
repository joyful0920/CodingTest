import sys
si = sys.stdin.readline

n = int(si())

# for문 사용
# for i in range(0, n):
#     print('*' * (n - i))

#리스트 컴프리헨션 사용
[print('*' * (n - i)) for i in range(0, n)]