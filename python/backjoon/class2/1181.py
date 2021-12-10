n = int(input())
a = []

for i in range(n):
    a.append(input())
a = set(a)
a_list = sorted(list(a))
a_list.sort(key=lambda x : len(x))
for i in a_list:
    print(i)