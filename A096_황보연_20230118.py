#https://leetcode.com/problems/number-of-1-bits/submissions/880278694/

class Solution:
    def hammingWeight(self, n: int) -> int:
        # print(bin(n))

        b_n = str(bin(n))

        list_a = list(b_n)
        # print(list_a)
        
        return list_a.count("1")