from sys import stdin

n = int(input())
m = list(map(int, sys.stdin.readline().split()))

x = int(input())
y = list(map(int, sys.stdin.readline().split()))

for i in range(x):
    print(m.count(y[i]), end=" ")

# 두 번째 방법
n = stdin.readline().rstrip()
card = list(map(int, stdin.readline().split()))
m = stdin.readline().rstrip()
test = list(map(int, stdin.readline().split()))

hash = {}

for i in card:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in test:
    if i in hash:
        print(hash[i], end=' ')
    else:
        print(0, end=' ')
