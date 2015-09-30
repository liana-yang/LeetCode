class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
        	return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for i in range(n)] for i in range(m)]
        maxSize = 0
        for j in range(n):
        	dp[0][j] = int(matrix[0][j])
        	maxSize = max(maxSize, dp[0][j])
        for i in range(1, m):
        	dp[i][0] = int(matrix[i][0])
        	maxSize = max(maxSize, dp[i][0])
        for i in range(1, m):
        	for j in range(1, n):
        		if matrix[i][j] == '1':
        			dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        			maxSize = max(maxSize, dp[i][j])
        return maxSize * maxSize

s = Solution()
print s.maximalSquare([['1','0','1','0','0'],['1','0','1','1','1'],['1','1','1','1','1'],['1','0','0','1','0']])