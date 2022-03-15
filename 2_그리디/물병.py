import sys
si = sys.stdin.readline

n, k = map(int, si().split())
result = 0

# n을 이진수로 변환했을 때 1의 개수가 k보다 큰 경우 계속 반복
while bin(n).count('1') > k:
    # 이진수를 거꾸로 뒤집고 1의 인덱스 중 가장 작은 수로 2의 index 제곱한 값이
    # 반복마다 추가할 물병의 수
    new_bottle = 2 ** (bin(n)[::-1].index('1'))
    result += new_bottle
    n += new_bottle

print(result)