class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        '''
    	from up to down, then left to right

    	0   1   11  110
            	10  111
                	101
                	100

    	start:      [0]
    	i = 0:      [0, 1]
    	i = 1:      [0, 1, 3, 2]
    	i = 2:      [0, 1, 3, 2, 6, 7, 5, 4]
    	'''
    	
        result = [0]
        for i in range(n):
        	length = len(result)
        	for j in range(length):
        		result.append(result[length - 1 - j] + pow(2, i))
        return result



s = Solution()
print s.grayCode(2)