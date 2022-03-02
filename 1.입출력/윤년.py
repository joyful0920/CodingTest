import sys
si = sys.stdin.readline

year = int(si())

def leap():
    result = 0
    if (year % 4 == 0) and (year % 100 != 0):
        result = 1
    if year % 400 == 0:
        result = 1
    return result

print(leap())