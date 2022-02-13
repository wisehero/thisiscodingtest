import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.reverse()

answer = 0
i = 0
while k != 0:
    if coins[i] > k:
        i += 1
    else:
        answer += k // coins[i]
        k = k % coins[i]

print(answer)
