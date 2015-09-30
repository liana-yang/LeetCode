class Solution(object):
	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		# p is the parenthesis-string built so far, 
		# left and right tell the number of left and right parentheses still to add, 
		# and result collects the parentheses.
		def generate(p, left, right, result = []):
			if left:
				generate(p + '(', left - 1, right)
			if right > left:
				generate(p + ')', left, right - 1)
			if not right:
				result.append(p)
			return result
		return generate('', n, n)

s = Solution()
print s.generateParenthesis(3)