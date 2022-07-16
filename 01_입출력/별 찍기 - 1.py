import sys
si = sys.stdin.readline

# for문 사용
# n = int(si())

# for i in range(1, n + 1):
# 		print('*' * i)

#리스트 컴프리헨션 사용
[print('*' * i) for i in range(1, int(si()) + 1)]