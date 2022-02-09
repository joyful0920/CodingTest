import sys
si = sys.stdin.readline

# 테스트 케이스가 주어지지 않는 경우
while True:
    try:
        a, b = map(int, si().split())
        print(a + b)
    except:
        break