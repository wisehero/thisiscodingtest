from itertools import combinations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
answer_list = []

choice = list(combinations(nums, 3))

for i in range(len(choice)):
    if sum(choice[i]) <= m:
        answer_list.append(sum(choice[i]))

answer_list.sort()
print(answer_list[-1])
