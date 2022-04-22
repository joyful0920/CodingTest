import sys
si = sys.stdin.readline

n = int(si())

def hanoi(n, a, b, c): # (남은 원반수, 시작, 목표, 보조)
    if n == 1: # 원반이 하나일 때
        print(a, b)
        return
    hanoi(n - 1, a, c, b) # 밑바닥 원반을 제외하고 나머지 원반은 모두 보조로 이동
    print(a, b) # 마지막 남은 원반을 목표로 이동
    hanoi(n - 1, c, b, a) # 보조에 있는 원반을 목표로 이동시키기 위해 시작점과 보조를 체인지

print(2 ** n - 1) # 최소이동횟수 점화식
hanoi(n, 1, 3, 2)