import sys
si = sys.stdin.readline

s = si().rstrip()
result = 0

for i in s: # enumerate -> 인덱스와 밸류로 나눠서 접근 가능
    # i가 0이나 1이면 곱하는 것보다 더하는 것이 나음
    if i == '0' or i == '1':
        result += int(i)
    # 그게 아닌 경우
    else:
        # 기존 결과 값이 0인 경우는 곱할 수 없으므로 더하기
        if result == 0:
            result += int(i)
        # 그 외엔 무조건 곱하는 것이 나음
        else:
            result *= int(i)

print(result)