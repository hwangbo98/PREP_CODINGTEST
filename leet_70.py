
# 얼마 없을 때는 recursive가 더 빠름.

class Solution:
    
    def climbStairs(self, n: int) -> int:
        def fib_dp(n) :
            if n == 0 :
                return 1
            elif n == 1 :
                return 2

            fib_arr = [1,2]

            for i in range(2,n+1) :
                num = fib_arr[i-2] + fib_arr[i-1]
                fib_arr.append(num)
            return fib_arr[n]
        fib_arr= [1,2]
        def rec_fib_dp(n) :
            if n < len(fib_arr) :
                return fib_arr[n]
            
            else :
                fib = rec_fib_dp(n-1) + rec_fib_dp(n-2)
                fib_arr.append(fib)
                return fib

        return rec_fib_dp(n-1)