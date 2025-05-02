class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0]*n  for i in range(m)]
        matrix[-1][-1] = 1
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i+1 < m and j+1 < n:
                    matrix[i][j] = matrix[i+1][j] + matrix[i][j+1]
                elif j+1 < n:
                    matrix[i][j] =  matrix[i][j+1]
                elif i+1 <m :
                    matrix[i][j] =  matrix[i+1][j]
            
        
        return matrix[0][0]