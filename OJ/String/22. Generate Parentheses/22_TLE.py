class Solution(object):
	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		result = []
		flag = False
		if n == 0:
			return result
		else:
			queue = ['()', '#']
			count = 1
			while queue:
				temp = queue[0]
				del queue[0]
				if queue[0] == '#':
					del queue[0]
					count += 1
					flag = True
				queue.append('(' + temp + ')')
				if '()' + temp != temp + '()':
					queue.append('()' + temp)
				queue.append(temp + '()')
				if count == n:
					return queue
				if flag:
					queue.append('#')
					flag = False

s = Solution()
print s.generateParenthesis(3)