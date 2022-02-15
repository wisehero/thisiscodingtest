from itertools import accumulate

n = int(input())

times = list(map(int, input().split()))

times.sort()

# 누적합
print(sum(list(accumulate(times))))
