class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        set_list = list(set(nums))
        dict_a = {}
        for k in set_list :
            dict_a[k] = nums.count(k)
        sorted_dict = sorted(dict_a.items(), key = lambda item : item[1], reverse=True)
        first_key = next(iter(sorted_dict))

        return first_key[0]