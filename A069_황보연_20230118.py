N, K = map(int, input().split())

list_N = [i for i in range(1, N+1)]
result  = []
count = 0
while(len(list_N)>0) :
    count+=K-1
    if(count< len(list_N)) :
        result.append(list_N[count])
        del list_N[count]
    else :
        count%=len(list_N)
        result.append(list_N[count])
        del list_N[count]

count_list = 0
print("<", end="")
for i in result :
    if(count_list == len(result)-1) :

        print(str(i), end= "")
    else :
        print(str(i), end=", ")
    count_list+=1
print(">")