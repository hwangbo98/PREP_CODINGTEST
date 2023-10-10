class Solution:
    def removeDuplicates(self, s: str) -> str:
        k = 0
        list_s = [k for k in s]
        
        
        while k <len(list_s) -1 :
            if list_s[k] == list_s[k+1] :
                list_s.pop(k)
                list_s.pop(k)
                
                if k == 0 :
                    pass
                else :
                    k-=1
            else :
                k+=1
        print(list_s)

        return ''.join(list_s)