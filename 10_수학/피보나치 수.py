import sys
si = sys.stdin.readline

n = int(si())
numbers = [0] * (n + 1)
numbers[1] = 1

def fibonacci(i, numbers):
    numbers[i] = numbers[i - 1] + numbers[i - 2]
    if i < n:
        return fibonacci(i + 1, numbers)
    else:
        return numbers[i]

if n == 1:
    print(numbers[1])
else:
    print(fibonacci(2, numbers))