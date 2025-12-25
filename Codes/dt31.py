def solve():
    target = 200
    coins = [1, 2, 4, 10, 20, 40, 100]

    # dp[i] will store the number of ways to make value i
    dp = [0] * (target + 1)
    dp[0] = 1 # Base case: one way to make zero

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]

    return dp[target]

print(solve())
