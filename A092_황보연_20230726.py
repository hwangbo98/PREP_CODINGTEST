class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        k = 0
        result = []
        for i in nums :
            if i%2 == 0 :
                result.append(i)
                result.append(0)
                k+=2
        k =1
        for i in nums :
            if i%2!=0 :
                result[k] = i
                k+=2

        print(result)

        return result