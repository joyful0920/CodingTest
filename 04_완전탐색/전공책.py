from copy import deepcopy
import sys
si = sys.stdin.readline

t = si().rstrip()
n = int(si())

books = []
for _ in range(n):
    price, name = map(str, si().split())
    books.append([int(price), name])
books.sort(reverse=True)

bookname = []
for i in range(n):
    bookname.append(list(map(str, books[i][1])))
min_price = []
for i in range(len(t)):
    min_price.append((0, 0))

for i in range(n):
    price_copy = deepcopy(min_price)
    new = False
    s = []
    for j in range(len(t)):
        s.append([t[j], False])
    for j in range(len(bookname[i])):
        for k in range(len(t)):
            if bookname[i][j] == t[k] and s[k][1] == False:
                if price_copy[k][0] == 0:
                    new = True
                bookname[i][j] = ' '
                s[k][1] = True
                price_copy[k] = (books[i][0], i)
                break
    if new:
        min_price = price_copy
    else:
        temp1 = list(set(min_price))
        temp2 = list(set(price_copy))
        temp1_price = [temp1[j][0] for j in range(len(temp1))]
        temp2_price = [temp2[j][0] for j in range(len(temp2))]
        if sum(temp1_price) > sum(temp2_price):
            min_price = price_copy

result = list(set(min_price))
result_price = [result[i][0] for i in range(len(result))]
if (0, 0) in result:
    print(-1)
else:
    print(sum(result_price))