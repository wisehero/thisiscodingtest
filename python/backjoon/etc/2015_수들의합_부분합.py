import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
answer = 0
sum_arr = [0] * n
sum_arr[0] = arr[0]
for i in range(1, len(arr)):
    sum_arr[i] = sum_arr[i - 1] + arr[i]

count = {}
for i in range(n):
    goal = sum_arr[i] - m

    if goal in count:
        answer += count[goal]
    if goal == 0:
        answer += 1

    if sum_arr[i] not in count:
        count[sum_arr[i]] = 0
    count[sum_arr[i]] += 1


print(answer)
