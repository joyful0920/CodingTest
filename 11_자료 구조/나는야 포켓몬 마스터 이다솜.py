import sys
si = sys.stdin.readline

n, m = map(int, si().split())
name = dict()
num = dict()

for i in range(1, n + 1):
    pokemon = si().rstrip()
    name[i] = pokemon
    num[pokemon] = i

for _ in range(m):
    target = si().rstrip()
    if target.isdecimal() == True:
        print(name[int(target)])
    else:
        print(num[target])