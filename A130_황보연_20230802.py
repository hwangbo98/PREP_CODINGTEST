#백준 10773번 제로! 

import sys

input = sys.stdin.readline

n = int(input())
result = []
for i in range(n) :
    num = int(input())
    if(num == 0) :
        if(len(result) == 0 ) :
            pass
        else :
            result.pop()

    else :
        result.append(num)


print(sum(result))

