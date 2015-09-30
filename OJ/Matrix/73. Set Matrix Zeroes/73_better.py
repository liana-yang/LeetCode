class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        col0 = 1
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        i = rows - 1
        while i >= 0:
            j = cols - 1
            while j >= 1:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                j -= 1
            if col0 == 0:
                matrix[i][0] = 0
            i -= 1


if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.setZeroes([[0,1,2],[2,1,3]])
    finish = clock()
    print (finish - start) * 1000