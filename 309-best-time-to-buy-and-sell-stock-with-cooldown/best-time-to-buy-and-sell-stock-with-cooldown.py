class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        # memo = {}
        dp = [[0,0] for _ in range (n + 2)]

            # if (i, flag) in memo:
            #     return memo[(i, flag)]

        for i in range(n-1, -1, -1) :
            dp[i][1] = max(prices[i] + dp[i+2][0], dp[i+1][1])
            dp[i][0] = max(-prices[i] + dp[i+1][1], dp[i+1][0])
        return dp[0][0] 

        #     if flag: 
        #         sell = prices[i] + solve(i + 2, False)
        #         hold = solve(i + 1, True)
        #         memo[(i, flag)] = max(sell, hold)
        #     else:     
        #         buy = -prices[i] + solve(i + 1, True)
        #         skip = solve(i + 1, False)
        #         memo[(i, flag)] = max(buy, skip)

        #     return memo[(i, flag)]

        # return solve(0, False)