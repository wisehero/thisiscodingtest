import statistics
import sys
from collections import Counter

n = int(input())
lst = []

for _ in range(n):
    lst.append(int(sys.stdin.readline()))
lst.sort()
c = Counter(lst)

print(round(statistics.mean(lst)))
print(round(statistics.median(lst)))
if len(c) > 1 and c.most_common(2)[0][1] == c.most_common(2)[1][1]:
    print(c.most_common(2)[1][0])
else:
    print(c.most_common(1)[0][0])
print(max(lst) - min(lst))

