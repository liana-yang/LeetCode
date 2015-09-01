class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix): # clockwise rotate
        n = len(matrix)
        for i in range(n / 2): # first reverse up to down, then swap the symmetry
            matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return None

        # anticlockwise rotate
        # # first left up to right, then swap the symmetry

if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    print s.rotate([[1,2],[3,4]])
    print s.rotate([[1]])
    finish = clock()
    print (finish - start) * 1000