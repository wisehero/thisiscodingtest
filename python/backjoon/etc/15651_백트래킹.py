from itertools import product

n, m = map(int, input().split())

arr = list(product(list(range(1, n + 1)), repeat=m))

for a in arr:
    for j in range(len(a)):
        print(a[j], end=' ')
    print()
