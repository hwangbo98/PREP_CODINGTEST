# 백준 9095번 Dynamic Programming 동적할당

import sys
def fib_dp(n) :
    if n == 0 :
        return 1;
    elif n == 1 :
        return 2
    elif n == 2 :
        return 4
    fib_array = [1,2,4]

    for i in range(3, n+2) :
        num = fib_array[i-3] + fib_array[i-2] + fib_array[i-1]
        fib_array.append(num)

    return fib_array[n]

fib_array =[1,2,4]

def fib_recur_dp(n) :
    if n < len(fib_array) :
        return fib_array[n]
    
    else :
        fib = fib_recur_dp(n-1) + fib_recur_dp(n-2) + fib_recur_dp(n-3)
        fib_array.append(fib)
        return fib

input = sys.stdin.readline

result = []
result_1 = []

n = int(input())
for i in range(n) :
    num = int(input())
    # result.append(fib_dp(num-1))
    # result_1.append(fib_recur_dp(num-1))
    print(fib_dp(num-1))


# for k in range(len(result)) : 
#     print(result[k])
#     print(result_1[k])