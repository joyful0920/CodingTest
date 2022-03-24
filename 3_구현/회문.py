import sys
si = sys.stdin.readline

t = int(si())

def second(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def first(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            check1 = second(word, left + 1, right)
            check2 = second(word, left, right - 1)
            if check1 or check2:
                return 1
            else:
                return 2
    return 0

for _ in range(t):
    s = si().rstrip()
    left = 0
    right = len(s) - 1
    result = first(s, left, right)
    print(result)