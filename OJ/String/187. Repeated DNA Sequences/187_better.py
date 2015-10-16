class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        numDict = {"A": 0, "C": 1, "G": 2, "T": 3}
        result = []
        currCount = {}
        currNum = 0
        for i in range(10):
        	currNum = (currNum << 2) | numDict[s[i]]
        currCount[currNum] = 1
        for i in range(1, len(s) - 9):
            currNum = (currNum & 0x3ffff) << 2 | numDict[s[i + 9]]
            if currNum in currCount and currCount[currNum] == 1:
                result.append(s[i: i + 10])
                currCount[currNum] += 1
            elif currNum not in currCount:
                currCount[currNum] = 1
        return result

        """
        https://en.wikipedia.org/wiki/Rolling_hash
        """

s = Solution()
print s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
print s.findRepeatedDnaSequences("AAAAAAAAAAA")