import sys
si = sys.stdin.readline

a, b = map(int, si().split())

def comparison():
    if a > b:
        result = '>'
    elif a < b:
        result = '<'
    else:
        result = '=='
    return result
    
print(comparison())