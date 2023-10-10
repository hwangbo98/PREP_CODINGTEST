
A, B = map(int, input().split())

# print(f'A = {A} B= {B}')

def A_2_B(A, B) :
    count = 0
    while(B > A) :
        if B%2 == 0 :
            B/=2
            count+=1
        else :
            B-=1
            B/=10
            count+=1
        
        if B == A :
            return count + 1
    
    return -1

result = A_2_B(A,B)
print(result)
    
