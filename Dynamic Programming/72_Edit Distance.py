class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        matrix = [[0 for _ in range(len(word1))] for _ in range(len(word2))]
        
        n = len(word2)
        for row in matrix:
            row.append(n)
            n -= 1
        
        base = list(range(len(word1), -1, -1))
        matrix.append(base)
        
        for i in range(len(word2)-1,-1,-1):
            for j in range(len(word1)-1,-1,-1):
                if word2[i] == word1[j]:
                    matrix[i][j] = matrix[i+1][j+1]
                else:
                    matrix[i][j] = 1 +  min(matrix[i+1][j],matrix[i+1][j+1],matrix[i][j+1])
        
        
        
        
        return matrix[0][0]