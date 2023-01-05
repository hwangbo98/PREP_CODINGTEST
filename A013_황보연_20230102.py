class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = list(set(nums))
        dic = {}

        for i in nums :
            if i in dic :
                dic[i] +=1
            else :
                dic[i] = 1
        keys = list(dic.keys())
        value = list(dic.values())

        position = value.index(1)
        print(position)
        return keys[position]
        