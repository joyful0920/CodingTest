import sys
si = sys.stdin.readline

r = 31
m = 1234567891
total = 0

l = int(si())
array = list(map(str, str(si().rstrip())))

for i in range(l):
    total += (ord(array[i]) - 96) * (r ** i)

print(total % m)