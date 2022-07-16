import sys
si = sys.stdin.readline

n = int(si())

grade = []
for _ in range(n):
    n, k, e, m = map(str, si().rstrip().split())
    grade.append((n, int(k), int(e), int(m))) # 이름, 국어, 영어, 수학 순의 튜플을 저장

# 람다식을 사용하여 주어진 조건에 맞게 정렬
sorted_grade = sorted(grade, key = lambda x : (-x[1], x[2], -x[3], x[0]))

# 이름만 출력
for i in sorted_grade:
    print(i[0])