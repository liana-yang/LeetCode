class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        n = len(triangle)
        minlen = triangle[n - 1]
        layer = n - 2
        while layer >= 0: # for each layer
            for i in range(layer + 1): # check its every node
                # find the lesser of its two childer, and sum the current value in the triangle with it
                minlen[i] = min(minlen[i], minlen[i + 1]) + triangle[layer][i]
            layer -= 1
        return minlen[0]

if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
    #print s.minimumTotal([[-1],[2,3],[1,-1,-3]])
    finish = clock()
    print (finish - start) * 1000