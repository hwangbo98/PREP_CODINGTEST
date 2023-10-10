class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        count = 0
        for k in nums1 :
            count = 0
            if nums2.index(k) == len(nums2) -1 :
                res.append(-1)
            else :
                for j in range(nums2.index(k), len(nums2)) :
                    if nums2[nums2.index(k)] < nums2[j] :
                        res.append(nums2[j])
                        break
                    else :
                        count+=1
                        #res.append(-1)
                print(count)
                if count == len(nums2) - nums2.index(k)  :
                    res.append(-1)

        
        return res