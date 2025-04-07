class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(cost) > sum(gas):
            return -1

        curr = 0
        res = 0
        for i in range(0,len(gas)):
            curr = curr + (gas[i] - cost[i])
            
            if  curr < 0:
                curr = 0
                res = i+1

        return res 