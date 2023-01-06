
#https://leetcode.com/problems/self-dividing-numbers/submissions/872466280/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        count = 0
        for i in range(left, right+1) :
            a = [j for j in str(i)]
            print(a)
            if '0' in a :
                pass
            else :
                count = 0
                for k in a :
                    if i % int(k) == 0 :
                        count+=1
                if count == len(a) :
                    res.append(i)
        
        return res