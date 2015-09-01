class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    # 8:21
    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1

        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid / cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1

        return False


if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    #print s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],3)
    print s.searchMatrix([[-10,-8,-6,-4,-3],[0,2,3,4,5],[8,9,10,10,12]], 0)
    finish = clock()
    print (finish - start) * 1000