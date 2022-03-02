import sys
si = sys.stdin.readline

t = int(si())

for _ in range(t):
    ox = si()
    total = 0
    point = 0
    for i in range(len(ox)):
        if ox[i] == 'O':
            point += 1
            total += point
        else:
            point = 0
    print(total)
