#!/usr/bin/python3

def makeChange(coins, total):
    """ Generate changes needed to reach total

    Args:
        coins (List[int]): List of coin denominations available.
        total (int): Total amount needed to reach.

    Returns:
        int: Minimum number of coins needed to reach the total amount.
             Returns -1 if it's not possible to reach the total amount.
    """
    if total == 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
