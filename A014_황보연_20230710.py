#Single Number : https://leetcode.com/problems/single-number/ LeetCode 136
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = list(set(nums))
        
        for i in result :
            if(nums.count(i) == 1) :
                return i 