import heapq
import sys

n = int(input())

heap = []

for _ in range(n):
    m = int(sys.stdin.readline())
    if len(heap) == 0 and m == 0:
        print(0)
        continue
    if m == 0:
        print(heapq.heappop(heap))
        continue
    heapq.heappush(heap, m)
