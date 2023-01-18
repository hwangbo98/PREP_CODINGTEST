# 백준 2839번 설탕 배달

n = int(input())

count = 0

if n % 5 == 0 :
    count = n // 5 

else :
    while n > 0 :
        n-=3
        count+=1
        if n%5 == 0 :
            count += n//5
            break
        
        elif n == 1 or n == 2 :
            count = -1
            break
        # elif n%3 == 0 :
        #     count += n//3 
        #     break


print(count)


    


