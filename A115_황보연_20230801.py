class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {}

        b = 0
        a = 0
        l = 0
        o = 0
        n = 0
        for j in text :
            if j == 'b' :
                b+=1
            elif j == 'a' :
                a+=1
            elif j =='l' :
                l+=1
            elif j == 'o' :
                o+=1
            elif j == 'n' :
                n+=1
            

        count = 0

        print(f'b = {b} a = {a} l = {l} o = {o} n = {n}')
        while b >= 1 and a >= 1 and l >= 2 and o>=2 and n >=1  :
            b-=1
            a-=1
            l-=2
            o-=2
            n-=1
            count+=1

        return count