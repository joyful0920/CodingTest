import sys
si = sys.stdin.readline

n, m = map(int, si().split())
set1 = set(si().rstrip() for _ in range(n))
set2 = set(si().rstrip() for _ in range(m))

unknown = set1 & set2
unknown = sorted(list(unknown))

print(len(unknown))
for i in unknown:
    print(i)