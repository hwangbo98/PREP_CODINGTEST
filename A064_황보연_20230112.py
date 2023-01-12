class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        expected = sorted(heights)
        count = 0
        for k, one in enumerate(heights) :
            if one != expected[k] :
                count+=1

        
        return count