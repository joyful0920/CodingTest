import sys
si = sys.stdin.readline

t = int(si())
array = [0]

for i in range(t):
    a, b = map(int, si().split())
    array.append(a + b)
    
for i in range(1, t + 1):
    print('Case #' + str(i) + ': ' + str(array[i]))