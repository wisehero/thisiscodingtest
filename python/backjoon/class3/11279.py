import heapq
import sys

n = int(input())
h = []

for i in range(n):
    number = int(sys.stdin.readline())
    if number == 0 and len(h) == 0:
        print(0)
        continue
    elif number == 0:
        print(-heapq.heappop(h))
    else:
        heapq.heappush(h, -number)
