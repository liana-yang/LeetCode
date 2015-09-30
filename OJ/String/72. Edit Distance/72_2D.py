class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0 for i in range(l1 + 1)] for i in range(l2 + 1)]
        for i in range(1, l1 + 1):
        	dp[0][i] = i
        for i in range(1, l2 + 1):
        	dp[i][0] = i
        for i in range(1, l2 + 1):
        	for j in range(1, l1 + 1):
        		if word2[i - 1] == word1[j - 1]:
        			dp[i][j] = dp[i - 1][j - 1]
        		else:
        			dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
        return dp[l2][l1]

        """
        Use f[i][j] to represent the shortest edit distance between word1[0,i) and word2[0, j). 
        Then compare the last character of word1[0,i) and word2[0,j), 
        which are c and d respectively (c == word1[i-1], d == word2[j-1]):
        if c == d, then : f[i][j] = f[i-1][j-1]
        Otherwise we can use three operations to convert word1 to word2:            
        (a) if we replaced c with d: f[i][j] = f[i-1][j-1] + 1;
        (b) if we added d after c: f[i][j] = f[i][j-1] + 1;
        (c) if we deleted c: f[i][j] = f[i-1][j] + 1;
        """

s = Solution()
print s.minDistance("hot", "dota")
print s.minDistance("sea", "eat")