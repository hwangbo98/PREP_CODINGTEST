class Solution:
    def isValid(self, s: str) -> bool:
        list_str = list(s)
        # small = 0
        # mid = 0
        # big = 0
        save_list = []
        
        while (('()' in s) or ('{}' in s) or ('[]' in s)) : 
           s = s.replace("()", '').replace("{}", '').replace("[]", '')
        #    print(s)
        if len(s)!= 0 :
            return False
        else :
            return True

