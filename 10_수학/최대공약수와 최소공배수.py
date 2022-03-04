import sys, math
si = sys.stdin.readline

a, b = map(int, si().split())
ma = max(a, b)
mi = min(a, b)

while mi != 0:
    if ma % mi == 0 and min(a, b) % mi == 0:
        break
    mi -= 1


print(mi) # print(math.gcd(a, b))
print(a * b // mi) # print(math.lcd(a, b))