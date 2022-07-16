import sys
si = sys.stdin.readline

result = int(si())

def grade():
    if result // 10 >= 9:
        grade = 'A'
    elif result // 10 >= 8:
        grade = 'B'
    elif result // 10 >= 7:
        grade = 'C'
    elif result // 10 >= 6:
        grade = 'D'
    else:
        grade = 'F'
    return grade

print(grade())