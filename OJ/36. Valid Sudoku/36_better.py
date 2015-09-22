class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Three flags are used to check whether a number appear.
        # used1: check each row
        # used2: check each column
        # used3: check each sub-boxes
        used1 = [[0 for i in range(9)] for i in range(9)]
        used2 = [[0 for i in range(9)] for i in range(9)]
        used3 = [[0 for i in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    k = i / 3 * 3 + j / 3
                    if used1[i][num] or used2[j][num] or used3[k][num]:
                        return False
                    used1[i][num] = used2[j][num] = used3[k][num] = 1
        return True

       


s = Solution()
print s.isValidSudoku([".........","......3..","...18....","...7.....","....1.97.",".........","...36.1..",".........",".......2."])
print s.isValidSudoku(["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....",".15......",".....2...",".2.9.....","..4......"])