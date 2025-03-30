class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        while i < len(nums):
            curr = nums[i]
            next = nums[i]
            while(i<len(nums)-1 and nums[i]+1 == nums[i+1]):
                next = nums[i+1]
                i += 1
            
            if curr == next:
                    res.append(f"{curr}")
            else:
                res.append(f"{curr}->{next}")
                
            i+= 1
        return res

# class Solution:
#     def summaryRanges(self, nums: List[int]) -> List[str]:
#         if len(nums) == 0:
#             return []
#         res = []
#         low = nums[0]
#         high = nums[0]
#         for i in range(1,len(nums)):
#             if nums[i]-1 == nums[i-1]:
#                 high = nums[i]
#             else:
#                 if low == high:
#                     res.append(f"{low}")
#                 else:
#                     res.append(f"{low}->{high}")
#                 low = nums[i]
#                 high = nums[i]
        
#         if(low == high):
#             res.append(f"{low}")
#         else:
#             res.append(f"{low}->{high}")
        
        
#         return res