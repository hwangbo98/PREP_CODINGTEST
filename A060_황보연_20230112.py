class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for k in operations :
            if k == "C" :
                res.pop()
            elif k == "D" :
                res.append(res[-1]*2)
            elif k == "+" :
                res.append(res[-1] + res[len(res)-2])
            else :
                res.append(int(k))
        
        print(res)

        return sum(res)