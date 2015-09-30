class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        hashMap = {}
        for i in range(9):
        	for j in range(1, 10):
        		hashMap[str(j)] = 0
        	for j in range(9):
        		if board[i][j] != '.':
        			if hashMap[board[i][j]] == 0:
        				hashMap[board[i][j]] = 1
        			else:
        				return False
        for i in range(9):
        	for j in range(1, 10):
        		hashMap[str(j)] = 0
        	for j in range(9):
        		if board[j][i] != '.':
        			if hashMap[board[j][i]] == 0:
        				hashMap[board[j][i]] = 1
        			else:
        				return False
        for i in range(3):
        	for j in range(3):
        		for k in range(1, 10):
        			hashMap[str(k)] = 0
        		for k in range(3):
        			for l in range(3):
        				if board[k + 3 * i][l + 3 * j] != '.':
        					if hashMap[board[k + 3 * i][l + 3 * j]] == 0:
        						hashMap[board[k + 3 * i][l + 3 * j]] = 1
        					else:
        						return False
        return True
       


s = Solution()
print s.isValidSudoku([".........","......3..","...18....","...7.....","....1.97.",".........","...36.1..",".........",".......2."])
print s.isValidSudoku(["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....",".15......",".....2...",".2.9.....","..4......"])