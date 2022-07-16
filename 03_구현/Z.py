import sys
si = sys.stdin.readline

n, r, c = map(int, si().split())
result = 0

while n > 1:
    size = (2 ** n) // 2
    # 2사분면
    if r < size and c >= size:
        result += size ** 2
        c -= size
    # 3사분면
    elif r >= size and c < size:
        result += 2 * (size ** 2)
        r -= size
    # 4사분면
    elif r >= size and c >= size:
        result += 3 * (size ** 2)
        r -= size
        c -= size
    n -= 1

# 1사분면
if r == 0 and c == 0:
    print(result)
# 2사분면
elif r == 0 and c == 1:
    print(result + 1)
# 3사분면
elif r == 1 and c == 0:
    print(result + 2)
# 4사분면
else:
    print(result + 3)