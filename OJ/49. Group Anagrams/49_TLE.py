class Solution(object):
	def isAnagrams(self, str1, str2):
		if len(str1) != len(str2):
			return False
		hashMap = {}
		for c in str1:
			if c not in hashMap:
				hashMap[c] = 1
			else:
				hashMap[c] += 1

		for c in str2:
			if c not in hashMap:
				return False
			else:
				hashMap[c] -= 1
				if hashMap[c] < 0:
					return False
		#for c in hashMap:
			#if hashMap[c] != 0:
				#return False
		return True

	def groupAnagrams(self, strs):
		"""
		:type strs: List[str]
		:rtype: List[List[str]]
		"""
		if not strs:
			return [[]]
		strs.sort()
		result = []
		flag = False
		for s in strs:
			for c in result:
				if c and self.isAnagrams(s, c[0]):
					c.append(s)
					flag = True
			if flag == False:
				result.append([s])
			flag = False
		return result

s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

        