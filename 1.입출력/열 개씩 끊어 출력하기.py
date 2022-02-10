import sys
si = sys.stdin.readline

words = si().rstrip()

for i in range(0, len(words), 10):
    print(words[i:i + 10])