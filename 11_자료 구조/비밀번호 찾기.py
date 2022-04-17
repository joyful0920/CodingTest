import sys
si = sys.stdin.readline

n, m = map(int, si().split())
memo = dict() # key 값을 사용해 비밀번호를 찾기 위해 딕셔너리 자료구조 사용

for _ in range(n):
    site, pw = map(str, si().rstrip().split())
    memo[site] = pw # 사이트의 key 값에 비밀번호를 저장

for _ in range(m):
    print(memo[si().rstrip()]) # 인덱스를 사이트 이름으로 접근하면 비밀번호 출력 가능