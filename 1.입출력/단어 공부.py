import sys
from copy import deepcopy

si = sys.stdin.readline

word = si().rstrip()

array = [0] * 91

for i in range(len(word)):
    if ord(word[i]) > 90:
        array[ord(word[i]) - 32] += 1
    else:
        array[ord(word[i])] += 1

array_copy = deepcopy(array)
array_copy.sort()

def cal():
    max_cnt = 0
    max_alphabet = 0
    for i in range(65, 91):
        if array[i] > max_cnt:
            max_cnt = array[i]
            max_alphabet = i
    return max_alphabet

if array_copy[-1] == array_copy[-2]:
    print('?')
else:
    print(chr(cal()))