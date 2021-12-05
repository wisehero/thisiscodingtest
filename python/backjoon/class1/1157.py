import collections

s = input().lower()

d = collections.defaultdict(int)

for i in s:
    d[i] += 1

dvl = list(d.values())

if dvl.count(max(dvl)) == 1:
    print()