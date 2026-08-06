class Solution:
    def solve(self, coins, i, Target, n, memo):
        if Target == 0:
            return 1
        if i == n:
            return 0

        if (i, Target) in memo:
            return memo[(i, Target)]

        take = 0
        if coins[i] <= Target:
            take = self.solve(coins, i, Target - coins[i], n, memo)

        not_take = self.solve(coins, i + 1, Target, n, memo)

        memo[(i, Target)] = take + not_take
        return memo[(i, Target)]

    def change(self, amount: int, coins: list[int]) -> int:
        memo = {}
        return self.solve(coins, 0, amount, len(coins), memo)