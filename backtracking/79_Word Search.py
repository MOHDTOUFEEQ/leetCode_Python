class Solution:
    def exist(self, board, word):
        arr = [[True for j in range(len(board[i])) ] for i in range(len(board))]
        
        def backtracking(i,j,index):
            if index == len(word):
                return True
            
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or arr[i][j] is False or word[index] != board[i][j] or index > len(word):
                return False

            
            arr[i][j] = False
            
            result  = (
                        backtracking(i+1,j,index+1) or 
                        backtracking(i,j+1,index+1) or
                        backtracking(i,j-1,index+1) or
                        backtracking(i-1,j,index+1) 
                        ) 
                
            
            arr[i][j] = True
        
            return result
        
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if (board[i][j] == word[0] and backtracking(i,j,0)):
                    return True
                
                
        return False  