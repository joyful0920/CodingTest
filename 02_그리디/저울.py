import sys
si = sys.stdin.readline

n = int(si())
array = list(map(int, si().split()))

array.sort() # 추의 무게값들을 오름차순으로 정렬
target = 1 # target의 초기값은 1로

# 추 값들을 확인하면서
for i in array:
    # 측정 불가능한 값이 등장하면 그 즉시 반복문 탈출
    if target < i:
        break
    # 현재 확인하고 있는 추의 값을 target에 더해줌으로써 다음 target값 설정
    target += i

print(target)