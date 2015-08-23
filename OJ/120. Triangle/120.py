class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        result = 0
        if triangle:
            length = len(triangle)
            distance = [[triangle[0][0]]]
            for i in range(1, length):
                l = len(triangle[i])
                distance.append([])
                for j in range(l):
                    if j == 0:
                        distance[i].append(triangle[i][j] + distance[i - 1][0])
                    elif j == l - 1:
                        distance[i].append(triangle[i][j] + distance[i - 1][l - 2])
                    else:
                        distance[i].append(triangle[i][j] + min(distance[i - 1][j], distance[i - 1][j - 1]))
        #print distance
        result = min(distance[length - 1])
        return result

if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
    #print s.minimumTotal([[-1],[2,3],[1,-1,-3]])
    finish = clock()
    print (finish - start) * 1000