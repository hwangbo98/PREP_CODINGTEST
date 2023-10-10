class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    
        count = nums.count(val)

        for k in nums :
            if k == val :
                for j in range(count) :
                    nums.remove(k)
        print(nums)
        return len(nums)