#백준 1193번 분수찾기 https://www.acmicpc.net/problem/1193

num = int(input())
sum_num  = 0
i = 0
while(sum_num<num) :
    i+=1
    sum_num+=i
    
# start _ end
start_value = 0 
end_value = 0
for k in range(0,i+1) :
    end_value +=k

start_value = end_value - i + 1


if i%2 ==0 :
    numerator = 0 #분자
    denominator =i+1 #분모
else :
    numerator = i+1
    denominator = 0
for j in range(start_value, end_value+1) :
    if i%2 == 0 :
        numerator+=1
        denominator-=1
    else :
        numerator-=1
        denominator+=1

    if j == num :
        print(str(numerator) + "/" + str(denominator))
        break


