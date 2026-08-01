class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        memo = {}

        def solve(i, flag):
            if i >= n:
                return 0

            if (i, flag) in memo:
                return memo[(i, flag)]

            if flag: 
                sell = prices[i] + solve(i + 2, False)
                hold = solve(i + 1, True)
                memo[(i, flag)] = max(sell, hold)
            else:     
                buy = -prices[i] + solve(i + 1, True)
                skip = solve(i + 1, False)
                memo[(i, flag)] = max(buy, skip)

            return memo[(i, flag)]

        return solve(0, False)