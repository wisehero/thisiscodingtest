from itertools import combinations

n, m = map(int, input().split())
numbers = list(x for x in range(1, n + 1))

for i in list(combinations(numbers, m)):
    for j in i:
        print(j, end=" ")
    print()
