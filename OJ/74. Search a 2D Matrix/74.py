class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        result = False
        if matrix:
            length = len(matrix)
            for i in range(length):
                if target >= matrix[i][0]:
                    if i == length - 1 or target < matrix[i + 1][0]:
                        for n in matrix[i]:
                            if n == target:
                                return True
        return result

if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],3)
    finish = clock()
    print (finish - start) * 1000