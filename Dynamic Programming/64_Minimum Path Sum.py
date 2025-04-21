class Solution:
    def minPathSum(self, grid) -> int:

        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[i])-1,-1,-1):    
        
                if (i + 1 < len(grid)) and (j + 1 < len(grid[i])):
                    minimum = min(grid[i+1][j],grid[i][j+1])
                    grid[i][j] = grid[i][j] + minimum
                elif j + 1 < len(grid[i]) :
                    grid[i][j] += grid[i][j + 1]
                elif (i + 1 < len(grid)):
                    grid[i][j] += grid[i+1][j]
                

        return grid[0][0]