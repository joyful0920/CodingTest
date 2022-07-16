import sys
si = sys.stdin.readline

n = int(si())
blacklist = []
whitelist = [1]

target = 1
while True:
    target += 1
    if len(whitelist) == n:
        break
    if target % 2 != 0 and target % 3 != 0 and target % 5 != 0:
        blacklist.append(target)
    else:
        if target // 2 in blacklist or target // 3 in blacklist or target // 5 in blacklist:
            blacklist.append(target)
        else:
            whitelist.append(target)

print(whitelist[-1])