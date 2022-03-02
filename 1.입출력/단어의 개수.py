import sys
si = sys.stdin.readline

string = si().rstrip()

def count():
    if len(string) == 0:
        cnt = 0
    else:
        cnt = 1
        for i in range(len(string)):
            if string[i] == ' ':
                cnt += 1
        if string[0] == ' ' or string[len(string) - 1] == ' ':
            cnt -= 1
    return cnt

print(count())