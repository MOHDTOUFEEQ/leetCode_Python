from collections import Counter
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rqueue = []
        dqueue = []
        
        for i in range(0,len(senate)):
            if senate[i] == 'R':
                rqueue.append(i)
            else:
                dqueue.append(i)
                
        n = len(senate)   
        while len(rqueue) > 0 and len(dqueue) > 0:
            if rqueue[0] < dqueue[0]:
                dqueue[0:1] = []
                rqueue[0:1] = []
                rqueue.append(n)
                n += 1
            else:
                dqueue[0:1] = []
                rqueue[0:1] = []
                dqueue.append(n)
                n += 1
        
        return "Radiant" if rqueue else "Dire"