import sys
si = sys.stdin.readline

n = int(si())
first = 666

# n이 0이 될 때까지 반복
while n != 0:
    if '666' in str(first):
        n -= 1
    if n == 0:
        break
    first += 1

print(first)