import sys
from collections import deque
si = sys.stdin.readline

n, k = map(int, si().split())
deq = deque() # deque 자료구조 활용
result = []

for i in range(1, n + 1):
    deq.append(i)

for i in range(n):
    deq.rotate(-k + 1) # deque의 ratate 함수를 활용하여 k번째 사람을 맨 앞 요소에 위치
    result.append(str(deq.popleft())) # 맨 앞 요소를 제거 후 결과 배열에 저장

print('<' + ', '.join(result) + '>')