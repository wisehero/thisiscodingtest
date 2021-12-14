import sys

n = int(sys.stdin.readline().rstrip())
n_list = [0] * 10001

for _ in range(n):
    data = int(sys.stdin.readline())
    n_list[data] += 1
for i in range(1, 10001):
    if n_list[i] != 0:
        for _ in range(n_list[i]):
            print(i)

