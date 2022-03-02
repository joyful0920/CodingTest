import sys
si = sys.stdin.readline

s = si().rstrip()

array = [-1] * 123

for i in range(len(s)):
    if array[ord(s[i])] == -1:
        array[ord(s[i])] = i

for i in range(97, 123):
    print(array[i], end=" ")