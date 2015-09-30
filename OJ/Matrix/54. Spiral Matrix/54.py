class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        result = []
        row = len(matrix)
        if row == 1:
            return matrix[0]
        elif row >= 2:
            column = len(matrix[0])
            i = 0
            j = 0
            up = 0
            down = row - 1
            left = 0
            right = column - 1
            count = 0
            temp = 2 * (down + right - up - left)
            #print "up = %s, down = %s, left = %s, right = %s" % (up, down, left, right)
            while count < row * column: 
                if count == temp and count != 0:
                    #print "i = %s, j = %s" % (i, j)
                    left += 1
                    right -= 1
                    up += 1
                    down -= 1
                    j += 1
                    i += 1
                    temp += 2 * (down + right - up - left)
                    #print "up = %s, down = %s, left = %s, right = %s" % (up, down, left, right)
                result.append(matrix[i][j])
                count += 1
                #print result
                if i == up:
                    if j == right:
                        i += 1
                    elif j == left:
                        j += 1
                    else:
                        j += 1
                elif i == down:
                    if j == right:
                        j -= 1
                    elif j == left:
                        i -= 1
                    else:
                        j -= 1
                else:
                    if j == right:
                        i += 1
                    elif j == left:
                        i -= 1
        return result

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