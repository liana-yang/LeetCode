class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        res = []
        if not matrix:
            return res
        rowBegin = 0
        rowEnd = len(matrix) - 1
        colBegin = 0
        colEnd = len(matrix[0]) - 1
        while rowBegin <= rowEnd and colBegin <= colEnd:
            # Traverse Right
            for i in range(colBegin, colEnd + 1):
                res.append(matrix[rowBegin][i])
            rowBegin += 1
            # Traverse Down
            for i in range(rowBegin, rowEnd + 1):
                res.append(matrix[i][colEnd])
            colEnd -= 1
            if rowBegin <= rowEnd:
                # Traverse Left
                i = colEnd
                while i >= colBegin:
                    res.append(matrix[rowEnd][i])
                    i -= 1
                rowEnd -= 1
            if colBegin <= colEnd:
                # Traver Up
                i = rowEnd
                while i >= rowBegin:
                    res.append(matrix[i][colBegin])
                    i -= 1
                colBegin += 1
        return res

if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
    print s.spiralOrder([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
    print s.spiralOrder([1])
    print s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    finish = clock()
    print (finish - start) * 1000