class Solution:
    def checkRecord(self, s: str) -> bool:
        new_s = list(s)
        if s.count('A') >= 2 :
            return False
        
        count = 0
        A_count = 0
        for k in new_s :
            if k == 'L' :
                count+=1
            elif k == 'A' :
                A_count+=1
                count = 0
            else :
                count = 0
            
            if count > 2 : 
                return False
            
        if count < 3 or A_count < 2 :
            return True
        print(count)