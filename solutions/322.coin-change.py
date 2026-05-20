# @leet start
import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX_INT = sys.maxsize

        # dp[i] = minimum number of coins required to make up i
        dp = [MAX_INT] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                j = i - coin
                if j < 0 or dp[j] == MAX_INT:
                    continue
                dp[i] = min(dp[i], dp[j] + 1)

        return dp[amount] if dp[amount] != MAX_INT else -1


# @leet end
