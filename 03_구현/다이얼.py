import sys
si = sys.stdin.readline

words = si().rstrip()
result = 0

for i in words:
    if i == 'A' or i == 'B' or i == 'C':
        result += 2
    elif i == 'D' or i == 'E' or i == 'F':
        result += 3
    elif i == 'G' or i == 'H' or i == 'I':
        result += 4
    elif i == 'J' or i == 'K' or i == 'L':
        result += 5
    elif i == 'M' or i == 'N' or i == 'O':
        result += 6
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        result += 7
    elif i == 'T' or i == 'U' or i == 'V':
        result += 8
    else:
        result += 9

print(result + len(words))