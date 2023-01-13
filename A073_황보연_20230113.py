class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for k in range(1,n+1) :
            if k%15 == 0 :
                result.append('FizzBuzz')
            elif k%5 == 0 :
                result.append('Buzz')
            elif k%3 == 0 :
                result.append('Fizz')
            else :
                result.append(str(k))

        return result