# https://leetcode.com/problems/search-insert-position/submissions/872516289/ 

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target not in nums :
            start = 0
            end = len(nums)- 1

            if target < nums[0] :
                return 0

            while start <= end :
                mid = (start + end) // 2

                if nums[mid] < target :
                    start = mid + 1
                else :
                    end = mid - 1
            return start

        else :
            start = 0
            end = len(nums)- 1

            while start <= end :
                mid = (start + end) // 2

                if nums[mid] == target :
                    return mid
                elif nums[mid] < target :
                    start = mid + 1
                else :
                    end = mid - 1