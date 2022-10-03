import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip())
array = list(map(int, input().split()))

cases = list(permutations(array, n))
result = 0

for case in cases:
    sum = 0
    for index in range(len(case) - 1):
        sum += abs(case[index] - case[index + 1])
    result = max(sum, result)

print(result)
