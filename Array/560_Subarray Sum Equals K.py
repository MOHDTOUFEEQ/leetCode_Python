class Solution:
    def subarraySum(self, nums, k):
        count = 0
        curr = 0
        mapp = {0:1}
        
        for i in nums:
            curr += i
            balance = curr - k 
            if balance in mapp:
                count += mapp[balance]
            
            mapp[curr] = mapp.get(curr, 0) + 1
        
        
        return count