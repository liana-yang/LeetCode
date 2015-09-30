class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        # travel all the words combinations to maintain a window
    	# there are wl(word len) times travel
    	# each time, n/wl words, mostly 2 times travel for each word
    	# one left side of the window, the other right side of the window
    	# so, time complexity O(wl * 2 * N/wl) = O(2N)
        result = []
        if not s:
        	return result
        k = len(words[0])
        hashMap = {}
        total = len(words)
        for i in range(len(s)):
        	for w in words:
        		hashMap[w] = 1
        	pos = i
        	count = 0
        	while pos < len(s):
        		# a more word, advance the window left side possiablly
        		if count == total:
        			# come to a result
        			result.append(pos - count * k)
        			break
        		temp = s[pos: pos + k]
        		# a valid word, accumulate results
        		if temp in hashMap and hashMap[temp] == 1:
        			# advance one word
        			hashMap[temp] = 0
        			count += 1
        			pos += k
        		else:
        			# not a valid word, reset all vars
        			break
        return result


s = Solution()
print s.findSubstring("barfoothefoobarman", ["foo", "bar"])