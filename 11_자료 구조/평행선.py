import sys
from collections import defaultdict
si = sys.stdin.readline

n = int(si())
# 딕셔너리의 기본값으로 빈 리스트 지정
x_dict = defaultdict(list)
y_dict = defaultdict(list)
result = 0

for _ in range(n):
    x, y = map(int, si().split())
    x_dict[x].append(y) # x좌표가 같은 y값끼리 하나의 리스트에 담기게 됨.
    y_dict[y].append(x) # y좌표가 같은 x값끼리 하나의 리스트에 담기게 됨.

# key값 마다 해당 value 리스트의 길이가 2를 넘어가면 전부 같은 직선으로 간주
for key in x_dict:
    if len(x_dict[key]) >= 2:
        result += 1

for key in y_dict:
    if len(y_dict[key]) >= 2:
        result += 1

print(result)