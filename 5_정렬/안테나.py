import sys
si = sys.stdin.readline

n = int(si())
houses = list(map(int, si().split()))

houses.sort() # 정렬 후

print(houses[(n - 1) // 2]) # 중간 지점값 출력