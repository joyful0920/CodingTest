import sys
si = sys.stdin.readline

n = int(si())
array = list(map(int, si().split()))
dic = dict()

m = int(si())
cards = list(map(int, si().split()))

for i in array:
    if i in dic: # array의 요소가 dic에 이미 존재한다면 해당 key의 value 1 증가
        dic[i] += 1
    else: # 존재하지 않았고 처음이라면 해당 value는 1
        dic[i] = 1

for i in cards:
    if i in dic: # 해당 카드가 dic에 존재한다면 해당 value 출력
        print(dic[i], end=' ')
    else: # 존재하지 않는다면 0 출력
        print(0, end=' ')