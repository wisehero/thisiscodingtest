from itertools import  permutations

n, m = map(int, input().split())
arr = list(permutations(list(range(1, n + 1)), m))

for a in arr:
    for j in range(len(a)):
        print(a[j], end=' ')
    print()
