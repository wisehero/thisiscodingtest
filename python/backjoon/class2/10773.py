n = int(input())
lst = []
for _ in range(n):
    m = int(input())
    if len(lst) == 0 and m == 0:
        continue
    if m == 0:
        lst.pop()
        continue
    lst.append(m)

print(sum(lst))
