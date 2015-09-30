class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for i in range(n)] for i in range(n)]
        if n == 0:
        	return matrix
        rowBegin = 0
        rowEnd = len(matrix) - 1
        colBegin = 0
        colEnd = len(matrix[0]) - 1
        count = 1
        while rowBegin <= rowEnd and colBegin <= colEnd:
            # Traverse Right
            for i in range(colBegin, colEnd + 1):
                matrix[rowBegin][i] = count
                count += 1
            rowBegin += 1
            # Traverse Down
            for i in range(rowBegin, rowEnd + 1):
                matrix[i][colEnd] = count
                count += 1
            colEnd -= 1
            if rowBegin <= rowEnd:
                # Traverse Left
                i = colEnd
                while i >= colBegin:
                    matrix[rowEnd][i] = count
                    count += 1
                    i -= 1
                rowEnd -= 1
            if colBegin <= colEnd:
                # Traver Up
                i = rowEnd
                while i >= rowBegin:
                    matrix[i][colBegin] = count
                    count += 1
                    i -= 1
                colBegin += 1
        return matrix

s = Solution()
print s.generateMatrix(3)