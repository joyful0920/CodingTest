import sys
si = sys.stdin.readline

n = int(si())

for i in range(1, n + 1):
    # i의 각 자릿수 더하기
    num = sum((map(int, str(i))))
    # 분해합 = 생성자 + 각 자릿수 합
    num_sum = i + num
    # 분해합과 입력과 입력값이 처음으로 같을 때 i 출력
    if num_sum == n:
        print(i)
        break
    # i값이 입력값과 같다는 건 생성자가 없다는 뜻
    if i == n:
        print(0)