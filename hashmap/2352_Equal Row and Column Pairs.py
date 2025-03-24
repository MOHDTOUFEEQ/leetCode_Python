class Solution:
    def equalPairs(self, grid):
        mapp = {}
        res = 0
        for r in range(0, len(grid)):
            vals = []
            for col in range(0, len(grid)):
                vals.append(grid[col][r])
            if tuple(vals) in mapp:
                mapp[tuple(vals)] += 1
            else:
                mapp[tuple(vals)] = 1
        
        for r in range(0, len(grid)):
            values = []
            for c in range(0, len(grid)):
                values.append(grid[r][c])
                
            if tuple(values) in mapp:
                res += mapp[tuple(values)]
            
                
        
        return res