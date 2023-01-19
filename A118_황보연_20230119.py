class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        for j,i in enumerate(nums) :
            if i == 0 :
                count+=1
                

        print(nums)
        for k in range(count) :
            nums.remove(0)
            nums.append(0)
        """
        Do not return anything, modify nums in-place instead.
        """