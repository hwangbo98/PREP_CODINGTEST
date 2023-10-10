
# https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # ans = log(n) / log(4)
        if(n<=0) :
            return False
        ans = log(n,4)

        print(ans)

        if ans == floor(ans) :
            return True
        else :
            return False