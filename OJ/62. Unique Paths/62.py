class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(n)] for i in range(m)]
        for i in range(0, n):
        	dp[0][i] = 1 
        for i in range(1, m):
        	dp[i][0] = 1
        for i in range(1, m):
        	for j in range(1, n):
        		dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m -1][n - 1]

s = Solution()
print s.uniquePaths(3, 7)
print s.uniquePaths(1, 1)