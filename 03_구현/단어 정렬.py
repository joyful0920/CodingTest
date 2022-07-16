import sys
si = sys.stdin.readline

n = int(si())
words = set()

for _ in range(n):
    words.add(si().rstrip())

words = list(words)
words.sort()
words.sort(key=lambda x:len(x))

for i in range(len(words)):
    print(words[i])