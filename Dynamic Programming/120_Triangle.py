class Solution:
    def minimumTotal(self, triangle) -> int:
        triangle.append([0] * (len(triangle) + 1))
        
        for i in range(len(triangle)-2,-1,-1):
            for index,val in enumerate(triangle[i]):
                triangle[i][index] = triangle[i][index] + min(triangle[i+1][index],triangle[i+1][index+1]) 
        
        return triangle[0][0]
        


# class Solution:
#     def minimumTotal(self, triangle) -> int:
#         res = 9999999999999
        
#         def backtracking(index, summ,row):
#             nonlocal res
            
#             if row == len(triangle):
#                 res = min(res,summ)
#                 return
            
#             if row > len(triangle):
#                 return
            
            
#             val1 = triangle[row][index]
#             backtracking(index,summ+val1,row+1)    
            
#             if index+1 < len(triangle[row]):
#                 val2 = triangle[row][index + 1]
#                 backtracking(index+1,summ+val2,row+1)    
             
        
#         backtracking(0, 0, 0)
        
        
        
#         return res