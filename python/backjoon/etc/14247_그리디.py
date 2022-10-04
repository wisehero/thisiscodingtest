import sys

n = int(sys.stdin.readline())
Hi = list(map(int, sys.stdin.readline().split()))
Ai = list(map(int, sys.stdin.readline().split()))
pair = []
for i in range(len(Hi)):
    pair.append(tuple([Hi[i], Ai[i]]))

pair = sorted(pair, key=lambda x: x[1])

sum = 0

for i in range(n):
    sum += pair[i][0] + i * pair[i][1]

print(sum)
