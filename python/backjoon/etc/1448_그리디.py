import sys

n = int(sys.stdin.readline())
length = [int(sys.stdin.readline()) for _ in range(n)]

length.sort()
answer = -1
for i in range(n - 1, 1, -1):
    if length[i] < length[i - 1] + length[i - 2]:
        answer = length[i] + length[i - 1] + length[i - 2]
        break

print(answer)
