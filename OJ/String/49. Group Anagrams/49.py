class Solution(object):
	def groupAnagrams(self, strs):
		"""
		:type strs: List[str]
		:rtype: List[List[str]]
		"""
		if not strs:
			return [[]]
		strs.sort()
		result = []
		hashMap = {}
		for s in strs:
			sorted_str = ''.join(sorted(s))
			if sorted_str in hashMap:
				hashMap[sorted_str].append(s)
			else:
				hashMap[sorted_str] = [s]
		for key in hashMap:
			if len(hashMap[key]) >= 1:
				result.append(hashMap[key])
		return result

s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

        