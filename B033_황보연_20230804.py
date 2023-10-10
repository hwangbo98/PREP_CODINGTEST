
n = int(input())

A = 0
B = 0 
C = 0

if n%10!=0 :
    print(-1)
else :
    while n > 0 :
        if n//300 >0 :
            A+= n//300
            n = n%300
        elif n//60 > 0 :
            B+= n//60 
            n = n%60 
        else :
            C+= n//10
            n = n%10

    print(A, B, C)
    