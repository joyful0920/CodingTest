import sys, math
si = sys.stdin.readline

n = int(si())

def prime_number(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def dfs(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(10):
            temp = num * 10 + i # 한자리 확장하고 일의 자리 0 ~ 9 테스트
            if prime_number(temp): # 소수라면
                dfs(temp) # 해당 수 기준으로 dfs 함수 호출

dfs(2)
dfs(3)
dfs(5)
dfs(7)