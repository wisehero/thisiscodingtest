import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(trees)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in trees:
        if x < mid:
            continue
        total += x - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
