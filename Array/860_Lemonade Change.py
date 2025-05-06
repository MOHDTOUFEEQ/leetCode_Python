class Solution:
    def lemonadeChange(self, bills) -> bool:
        count = {5:0,10:0}
        
        for i in bills:
            if i == 5:
                count[5] += 1
            elif i == 10:
                count[10] += 1
                if count[5] <= 0:
                    return False
                count[5] -= 1
            elif i == 20:
                if count[10] >= 1 and count[5] >= 1:
                    count[10] -= 1
                    count[5] -= 1
                elif count[5] >= 3:
                    count[5] -= 3
                else:
                    return False


        return True