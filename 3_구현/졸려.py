import sys
si = sys.stdin.readline

n = int(si())
words = si().rstrip()
length = len(words)
pattern = [words]

if length % 2 == 0:
    while True:
        words = words[0:length:2] + words[-1:0:-2]
        if words == pattern[0]:
            break
        pattern.append(words)
else:
    for _ in range(n):
        words = words[0:length+1:2] + words[-2:0:-2]
        if words == pattern[0]:
            break
        pattern.append(words)

print(pattern[n % len(pattern)])