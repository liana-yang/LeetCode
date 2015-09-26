class Solution:
    def f(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return self.f(n - 1) + self.f(n - 2)

    def f_iterative(self, n):
    	result = []
    	i = 1
    	while i <= n:
    		if i == 1:
    			result.append(1)
    		elif i == 2:
    			result.append(1)
    		else:
    			result.append(result[i - 2] + result[i - 3])
    		i += 1
    	return result

    	

s = Solution()
print s.f(6)
print s.f_iterative(6)