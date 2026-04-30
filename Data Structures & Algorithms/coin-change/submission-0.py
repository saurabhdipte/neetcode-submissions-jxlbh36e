class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float("inf")] * (amount + 1)
        dp[0]=0
        for coin in coins:
            for currentamt in range(coin, amount + 1):
                dp[currentamt]= min(dp[currentamt] , 1 + dp[currentamt-coin])
        return -1 if dp[amount]==float("inf") else dp[amount]