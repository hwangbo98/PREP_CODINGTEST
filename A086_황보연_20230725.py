#백준 1755번 숫자놀이 https://www.acmicpc.net/problem/1755

M, N = map(int, input().split())

list_M_N = [str(i) for i in range(M,N+1)]
result = {}
for k in list_M_N :
    number = ""
    for j in k :
        if(j =='1') :
            number+="one "
        elif(j =='2') :
            number+="two "
        elif(j=='3') :
            number+="three "
        elif(j=='4') :
            number+="four "
        elif(j=='5') :
            number+="five "
        elif(j=='6') :
            number+="six "
        elif(j=='7') :
            number+="seven "
        elif(j=='8') :
            number+="eight "
        elif(j=='9') :
            number+= "nine "
        else :
            number+= "zero "
    
    result[k] = number

sorted_result = sorted(result.items(), key = lambda x : x[1])
count = 1
for keys, values in sorted_result :
    if(count%10==0) :
        print(keys)
    else :
        print(keys, end =" ")
    count+=1