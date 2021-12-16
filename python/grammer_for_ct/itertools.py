import itertools

data = ['A', 'B', 'C']

result = list(itertools.permutations(data, 3))
result2 = list(itertools.combinations(data, 3))

print(result)
print(result2)
