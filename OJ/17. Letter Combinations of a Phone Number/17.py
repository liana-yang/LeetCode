class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        hashMap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
        	return []
        res = ['']
        for i in range(0, len(digits)):
            while res and len(res[0]) == i:
                for c in hashMap[digits[i]]:
                    res += [res[0] + c]
            	del res[0]
        return res

s = Solution()
print s.letterCombinations('23')