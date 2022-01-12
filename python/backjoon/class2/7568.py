n = int(input())
lst = []
r = 1
rank = []
for _ in range(n):
    a = map(int, input().split())
    lst.append(tuple(a))

for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            r += 1
    rank.append(r)
    r = 1

for i in rank:
    print(i, end=" ")
