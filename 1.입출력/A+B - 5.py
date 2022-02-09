import sys
si = sys.stdin.readline

t = int(si())
array = []

for i in range(t):
    a, b = map(int, si().split(','))
    array.append(a + b)
    
for i in range(t):
    print(array[i])