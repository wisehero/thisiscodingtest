import sys
from itertools import combinations

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

number = list(map(int, sys.stdin.readline().split()))
answer = 0
for i in list(combinations(number, 2)):
    if sum(i) == m:
        answer += 1

print(answer)
