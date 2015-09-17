import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
        	return 0
        passed = [False for i in range(n)]
        count = 1
        upper = math.sqrt(n)
        i = 3
        while i < n:
        	if not passed[i]:
        		count += 1
        		j = i * i
        		while j < n:
        			passed[j] = True
        			j += i
        	i += 2
        return count
s = Solution()
print s.countPrimes(10)