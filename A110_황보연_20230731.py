# 백준 거스름돈 5585번  https://www.acmicpc.net/problem/5585
coin = int(input())

remainder = 1000 - coin
result = 0
while(remainder>0) :
    if(remainder//500>0) :
        result+=remainder//500
        remainder= remainder%500
        
    elif(remainder//100>0) :
        result+=remainder//100
        remainder= remainder % 100
        
    elif(remainder//50>0) :
        result+=remainder//50
        remainder= remainder % 50
        
    elif(remainder//10>0) :
        result+=remainder//10
        remainder= remainder % 10
        
    elif(remainder//5>0) :
        result+=remainder//5
        remainder= remainder % 5
    
    elif(remainder//1>0) :
        result+=remainder//1
        remainder= 0
    

print(result)