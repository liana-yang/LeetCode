class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        row = len(matrix)
        column = 0
        if matrix:
            column = len(matrix[0])
        temp1 = [[] for i in range(row)]
        for i in range(row):
            for j in range(column):
                temp1[i].append(matrix[i][j])
        temp2 = [[r[i] for r in matrix] for i in range(column)]
        #print "row = %s, column = %s" % (row, column)
        for i in range(row):
            for j in range(column):
                if 0 in temp1[i] or 0 in temp2[j]:
                    matrix[i][j] = 0
        return None
        '''for i in range(row):
            print temp1[i]
        print "============="
        for i in range(column):
            print temp2[i]
        print "============="
        for i in range(row):
            print matrix[i]
        return 0'''


if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.setZeroes([[0,1,2],[2,1,3]])
    finish = clock()
    print (finish - start) * 1000