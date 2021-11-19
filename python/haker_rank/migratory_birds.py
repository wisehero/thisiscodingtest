from itertools import combinations

def divisibleSumPairs(n, k, ar):
    count = 0
    for i in combinations(ar,2):
        if sum(i)%k == 0:
            count += 1
    return count