region = int(input())
requests = list(map(int, input().split()))
budget = int(input())


def calculate_needed_budget(upper_bound):
    needed_budget = 0
    for request in requests:
        needed_budget += min(request, upper_bound)

    return needed_budget


low = 0
high = max(requests)
good_upper_bound = 0

while low <= high:
    mid = (low + high) // 2
    if calculate_needed_budget(mid) <= budget:
        good_upper_bound = mid
        low = mid + 1
    else:
        high = mid - 1

answer = 0
for requests in requests:
    given = min(requests, good_upper_bound)
    answer = max(answer, given)
print(answer)
