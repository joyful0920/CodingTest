import sys
si = sys.stdin.readline

t = int(si())

for _ in range(t):
    n = int(si())
    cnt = 0
    i = 5

    # 팩토리얼 의 0의 개수는 10(2*5)이 곱해지는 개수
    # 팩토리얼에서 2의 배수는 많으니 5가 곱해지는 횟수만 카운트하면 됨.
    # 25, 125같이 5가 아닌 5의 배수가 곱해지면 0의 개수는 2개, 3개... 복수가 추가가 됨.
    # n을 5의 제곱수로 계속 나눠준 값을 더해주는 방식으로 위의 복수 처리가 가능
    while i <= n:
        cnt += n // i
        i *= 5

    print(cnt)