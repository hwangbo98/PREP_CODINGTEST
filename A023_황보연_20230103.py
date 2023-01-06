#leetcode Add digits

class Solution:
    def addDigits(self, num: int) -> int:
        int_to_str = str(num)
        result = 0
        while(len(int_to_str) >= 2) :
            for i in int_to_str :
                result += int(i)
            int_to_str = str(result)
            result = 0
        
        return int(int_to_str)
        
       