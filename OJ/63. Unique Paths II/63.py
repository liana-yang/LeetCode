class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or obstacleGrid[0][0] == 1:
        	return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for i in range(m)]
        for i in range(0, n):
        	if obstacleGrid[0][i] == 0:
        		dp[0][i] = 1 
        	else:
        		break
        for j in range(1, m):
        	if obstacleGrid[j][0] == 0:
        		dp[j][0] = 1
        	else:
        		break
        for i in range(1, m):
        	for j in range(1, n):
        		if obstacleGrid[i][j] == 0:
        			dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m -1][n - 1]

s = Solution()
print s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
print s.uniquePathsWithObstacles([[0,0],[1,1],[0,0]])