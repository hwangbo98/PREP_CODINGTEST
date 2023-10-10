
# https://leetcode.com/problems/lemonade-change/submissions/872416859/ 

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        pocket = {5:0, 10:0, 15:0}

        for k in bills :
            if k == 5 :
                pocket[5] +=1
            elif k == 10 :
                if(pocket[5]>0) :
                    pocket[5] -=1
                    pocket[10]+=1
                else :
                    return False
            else :
                if (pocket[5] > 0 and pocket[10] > 0) :
                    pocket[5]-=1
                    pocket[10]-=1
                
                elif (pocket[5] > 2) :
                    pocket[5]-=3
                else :
                    return False

        return True
