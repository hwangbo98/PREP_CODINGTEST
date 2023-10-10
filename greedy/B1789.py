
S = int(input())
n = 0
sum_1 = 0
while(True) :
    sum_1+=n
    if(sum_1 > S) :
        break
    n+=1
print(n-1)