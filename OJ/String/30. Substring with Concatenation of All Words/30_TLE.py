class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # // travel all the words combinations to maintain a window
        # there are wl(word len) times travel
        # each time, n/wl words, mostly 2 times travel for each word
        # one left side of the window, the other right side of the window
        # so, time complexity O(wl * 2 * N/wl) = O(2N)
        result = []
        length = len(s)
        count = len(words)
        if length <= 0 or count <= 0:
            return result
        # init word occurence
        hashMap = {}
        for i in range(count):
            if words[i] not in hashMap:
                hashMap[words[i]] = 1
            else:
                hashMap[words[i]] += 1
        # travel all sub string combinations
        k = len(words[0])
        for i in range(k):
            left = i
            n = 0
            tempMap = {}
            j = i
            while j <= length - k:
                t = s[j: j + k]
                # a valid word, accumulate results
                if t in hashMap and hashMap[t] > 0:
                    if t not in tempMap:
                        tempMap[t] = 1
                    else:
                        tempMap[t] += 1
                    if tempMap[t] <= hashMap[t]:
                        n += 1
                    else:
                        # a more word, advance the window left side possiablly
                        while(tempMap[t] > hashMap[t]):
                            t1 = s[left: left + k]
                            tempMap[t1] -= 1
                            if tempMap[t1] < hashMap[t1]:
                                n -= 1
                            left += k
                    # come to a result
                    if n == count:
                        result.append(left)
                        tempMap[s[left: left + k]] -= 1
                        n -= 1
                        left += k
                # not a valid word, reset all vars
                else:
                    tempMap = {}
                    n = 0
                    left = j + k
                j += k
        return result   

s = Solution()
print s.findSubstring("barfoothefoobarman", ["foo", "bar"])