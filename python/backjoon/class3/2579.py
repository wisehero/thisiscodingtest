from itertools import product

n = int(input())

step = [1, 2]
scores = []  # 10 20 15 25 10 20

for _ in range(n):
    scores.append(int(input()))

scores_list = []

case = list(product(step, repeat=n - 3))

for i in case:
    if sum(i) != n - 1:
        case.remove(i)

for i in case:
    score = scores[0]
    score += scores[0 + i[0]] + scores[0 + i[0] + i[2]] + scores[0 + i[0] + i[1] + i[2]]
    scores_list.append(score)

scores_list.sort()
print(scores_list[-1])
