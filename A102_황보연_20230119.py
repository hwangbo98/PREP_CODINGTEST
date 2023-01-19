class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        # print(len(matrix[0]))

        small = len(matrix[0])
        big = len(matrix)
        
        res = []
        for k in range(small) :
            a = []
            for j in range(big) :
                a.append(matrix[j][k])
            res.append(a)

        return res