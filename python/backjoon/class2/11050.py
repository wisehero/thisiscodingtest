from itertools import combinations

a, b = map(int, input().split())
a_list = [x for x in range(1, a + 1)]
s = list(combinations(a_list, b))
print(len(s))
