import sys
si = sys.stdin.readline

people = [list(map(int, si().split())) for _ in range(10)]

max_people = 0
now_people = 0

for i in range(10):
    down, up = people[i]
    now_people -= down
    now_people += up
    max_people = max(max_people, now_people)

print(max_people)