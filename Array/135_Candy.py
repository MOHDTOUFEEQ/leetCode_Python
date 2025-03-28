class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [1 for i in ratings]
        
        for i in range(1, len(left)):
            if ratings[i]>ratings[i-1]:
                left[i] = left[i-1]+1
            
        for j in range(len(left)-2,-1,-1):
            if ratings[j] > ratings[j+1]:
                newVal = left[j+1] +1
                if(newVal > left[j]):
                    left[j] = newVal 
            
        
        return sum(left)
    

#  left = [1 for i in ratings]
        
#         for i in range(1, len(left)):
#             if ratings[i]>ratings[i-1]:
#                 left[i] = left[i-1]+1
#             elif ratings[i]<ratings[i-1]:
#                 for j in range(i-1,-1,-1):
#                     if(ratings[j]>ratings[j+1]):
#                         newVal = left[j+1]+1 
#                         if(newVal>left[j]):
#                             left[j] = newVal
#                         else:
#                             break
    
#         return sum(left)