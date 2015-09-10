class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        def dfs(curr, x, y):
            if curr == len(word):
                return True
            if x > 0 and board[x - 1][y] == word[curr]:
                board[x - 1][y],temp = '#',board[x - 1][y]
                if dfs(curr + 1, x - 1, y):
                    return True
                board[x - 1][y] = temp
            if x < len(board) - 1 and board[x + 1][y] == word[curr]:
                board[x + 1][y], temp = '#', board[x + 1][y]
                if dfs(curr + 1, x + 1,y):
                    return True
                board[x + 1][y] = temp
            if y > 0 and board[x][y - 1] == word[curr]:
                board[x][y - 1], temp = '#', board[x][y - 1]
                if dfs(curr + 1, x, y - 1):
                    return True
                board[x][y - 1] = temp
            if y < len(board[0]) - 1 and board[x][y + 1] == word[curr]:
                board[x][y + 1], temp = '#', board[x][y + 1]
                if dfs(curr + 1, x, y + 1):
                    return True
                board[x][y + 1] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    board[i][j],temp = '#', board[i][j]
                    if dfs(1, i, j):
                        return True
                    board[i][j] = temp
        return False
        
s = Solution()
print s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCCED')