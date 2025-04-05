import math
class Solution:
    def searchMatrix(self, matrix, target):
        left = 0
        right = len(matrix)-1
        while(left<right):
            mid = math.floor((left+right)/2)
            if(matrix[mid][-1] < target):
                left = mid + 1
            else:
                right = mid 
             
        l1 = 0        
        r1 = len(matrix[left]) - 1         
        while(l1<=r1):
            mid = math.floor((l1+r1)/2)
            if(matrix[left][mid] == target):
                return True
            
            elif(matrix[left][mid] > target):
                r1 = mid -1 
            else:
                l1 = mid + 1 
        
        return  False