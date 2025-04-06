class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 1
        
        points.sort(key= lambda x : x[1])
        
        curr = points[0][1]
        
        for i in range(1,len(points)):
            if points[i][0] > curr:
                res += 1
                curr = points[i][1]
        
        
        return res