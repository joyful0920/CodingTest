import sys
si = sys.stdin.readline

x, y = map(int, si().split())
weeks = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total = 0

for i in range(0, x - 1):
    total += days[i]

print(weeks[(total + y) % 7])