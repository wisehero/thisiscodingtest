n = int(input())
pos = []

for i in range(n):
    n, m = map(int, input().split())
    pos.append((n, m))

pos.sort()
pos.sort(key=lambda x: x[1])

for i in pos:
    print(i[0], i[1])
