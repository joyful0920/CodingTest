import sys
si = sys.stdin.readline

n = int(si())
array = sorted(list(map(int, si().split())))
groups = 0
members = 0

for i in array:
    members += 1 # 현재 그룹에 멤버 1명 추가
    if i == members: # 현재 검사 인원 공포도가 그룹 멤버수와 같아지면
        groups += 1 # 그룹 분리
        members = 0 # 멤버수 초기화

print(groups)