class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
        	return 0
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
        	dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

s = Solution()
print s.climbStairs(5)