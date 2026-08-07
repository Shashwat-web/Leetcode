class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        memo = {}
        def solve(i, j):
            if i >= n or j >= m:
                return 0

            if obstacleGrid[i][j] == 1:
                return 0

            if i == n - 1 and j == m - 1 :
                return 1 

            if (i,j) in memo :
                return memo[(i,j)] 

            down = solve(i + 1, j)
            right = solve(i, j + 1)

            memo[(i,j)] = down + right 
            return memo[(i,j)]

        return solve(0, 0)