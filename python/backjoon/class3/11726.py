n = int(input())
dp = [0] * 1001


def tile(m):
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    for i in range(3, 1001):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[m] % 10007


print(tile(n))
