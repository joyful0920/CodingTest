import sys
si = sys.stdin.readline

n, kim, yim = map(int, si().split())

def change_num(num):
    if num % 2 == 1:
        num = (num + 1) // 2
    else:
        num = num // 2
    return num

def star(kim, yim):
    cnt = 1
    while True:
        if kim % 2 == 1:
            if kim + 1 == yim:
                break
        if yim % 2 == 1:
            if yim + 1 == kim:
                break
        kim = change_num(kim)
        yim = change_num(yim)
        cnt += 1
    return cnt

print(star(kim, yim))