from itertools import combinations

x, y = map(int, input().split())
array = list(map(int, input().split()))
count = 0

for i in range(1, 21):
    comb = list(combinations(array, i))
    for j in comb:
        if sum(j) == y:
            count += 1

print(count)
