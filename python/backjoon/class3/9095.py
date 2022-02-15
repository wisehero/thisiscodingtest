# 정수 n이 주어졌을 때, n을 1,2,3의 합으로 나타내는 방법의 수

from itertools import product

t = int(input())
dp = [0, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504]

for _ in range(t):
    n = int(input())
    print(dp[n])