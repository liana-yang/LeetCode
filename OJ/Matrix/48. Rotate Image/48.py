class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        row = len(matrix)
        if matrix:
            column = len(matrix[0])
            temp = [[] for i in range(row)]
            for i in range(row):
                for j in range(column):
                    temp[i].append(matrix[0][j])
                del matrix[0]
            for i in range(column):
                matrix.append([])
                for j in range(row):
                    matrix[i].append(temp[row - 1 - j][i])
        #print temp
        #print matrix
        return None

if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.rotate([[1,2,3],[4,5,6]])
    print s.rotate([[1,2],[3,4]])
    print s.rotate([[1]])
    finish = clock()
    print (finish - start) * 1000