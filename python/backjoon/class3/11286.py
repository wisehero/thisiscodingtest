import heapq
import sys

result = []

n = int(sys.stdin.readline())

for _ in range(n):
    m = int(sys.stdin.readline())

    if m == 0 and len(result) == 0:
        print(0)
    elif m == 0:
        print(heapq.heappop(result)[1])
    else:
        heapq.heappush(result, (abs(m), m))
