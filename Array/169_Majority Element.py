# import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapping = {}
        num = []
        for i in nums:
            if i in mapping:
                mapping[i] += 1
            else:
                mapping[i] = 1
                num.append(i)
                
        res = 0
        value = None
        for j in num:
            if mapping[j] > res:
                res = mapping[j]
                value = j
                
                
        return value