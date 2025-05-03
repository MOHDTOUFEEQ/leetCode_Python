class Solution:
    def isValidSudoku(self, board) -> bool:
        def check(arr):
            number = [a for a in arr if a != "."]
            return len(set(number)) == len(number)
        
        # row
        for i in range(len(board)):
            if(check(board[i]) is False):
                return False
        # column
        for i1 in range(0,len(board)):
            arr = []
            for j1 in range(len(board)):
                arr.append(board[j1][i1])
            
            if(check(arr) is False):
                return False
        
        # box
        for i in range(0,len(board),3):
            for j in range(0,len(board[i]),3):
                arr1 = []
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        arr1.append(board[k][l])    
                    
                if(check(arr1) is False):
                    return False
            
            
        return True