class Solution:
    def increasingTriplet(self, nums) -> bool:
        res = False
        low = nums[0]
        high = None

        for i in nums:
            if i > low :
                if high is not None and i > high:
                    return True
                else:
                    high = i

            else:
                low = i

        return res