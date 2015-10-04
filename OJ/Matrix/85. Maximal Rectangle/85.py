class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        """
        https://leetcode.com/discuss/20240/share-my-dp-solution
        """
        if not matrix:
        	return 0
        m = len(matrix)
        n = len(matrix[0])
        left = [0 for i in range(n)]
        right = [n for i in range(n)]
        height = [0 for i in range(n)]
        maxSize = 0
        for i in range(m):
        	cur_left = 0
        	cur_right = n
        	for j in range(n): # compute height (can do this from either side)
        		if matrix[i][j] == '1':
        			height[j] += 1
        		else:
        			height[j] = 0

        	for j in range(n): # compute left (from left to right)
        		if matrix[i][j] == '1':
        			left[j] = max(left[j], cur_left)
        		else:
        			left[j] = 0
        			cur_left = j + 1

        	for j in range(n): # compute right (from right to left)
        		if matrix[i][n - 1 - j] == '1':
        			right[n - 1 - j] = min(right[n - 1 - j], cur_right)
        		else:
        			right[n - 1 - j] = n
        			cur_right = n - 1 - j
        	for j in range(n): # compute the area of rectangle (can do this from either side)
        		maxSize = max(maxSize, (right[j] - left[j]) * height[j])

        return maxSize
        """
        The DP solution proceeds row by row, starting from the first row. 
        Let the maximal rectangle area at row i and column j be computed by [right(i,j) - left(i,j)] * height(i,j).
        All the 3 variables left, right, and height can be determined by the information from previous row, 
        and also information from the current row. So it can be regarded as a DP solution. 
        The transition equations are:
        left(i,j) = max(left(i-1,j), curleft), curleft can be determined from the current row
        right(i,j) = min(right(i-1,j), curright), curright can be determined from the current row
        height(i,j) = height(i-1,j) + 1, if matrix[i][j]=='1';
        height(i,j) = 0, if matrix[i][j]=='0'
        """


s = Solution()
print s.maximalRectangle([['1','1','1','1','0'],['1','1','0','0','0'],['1','1','0','1','0'],['1','1','0','0','1']])
print s.maximalRectangle([['1','0','1','0','0'],['1','0','1','1','1'],['1','1','1','1','1'],['1','0','0','1','0']])