class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m = len(obstacleGrid) - 1 
        n = len(obstacleGrid[0]) - 1
        
        for i in range(len(obstacleGrid)-1,-1,-1):
            for j in range(len(obstacleGrid[i])-1,-1,-1):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                elif i == m and j == n:
                    obstacleGrid[i][j] = 1
                elif i + 1 <= m and j + 1 <= n:
                    obstacleGrid[i][j] = (obstacleGrid[i+1][j] + obstacleGrid[i][j + 1] )
                elif i + 1 <= m:
                    obstacleGrid[i][j] = obstacleGrid[i+1][j]
                elif j + 1 <= n:
                    obstacleGrid[i][j] = obstacleGrid[i][j+1]
                    
        
        return obstacleGrid[0][0]