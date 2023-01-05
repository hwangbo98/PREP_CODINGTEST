# 백준 2941번 크로아티아 알파벳  https://www.acmicpc.net/problem/2941
str_input = input()

i = 0
croatia_count=0
while(i<len(str_input)) :
    if(str_input[i:i+2] == "c=") :
        croatia_count+=1 
        i = i+2
    elif(str_input[i:i+2] == "c-") :
        croatia_count+=1
        i = i+2
    elif(str_input[i:i+3] == "dz=") :
        croatia_count+=1
        i = i+3
    elif(str_input[i:i+2] == "d-") :
        croatia_count+=1
        i = i+2
    elif(str_input[i:i+2] == "lj") :
        croatia_count+=1
        i = i+2
    elif(str_input[i:i+2] == "nj") :
        croatia_count+=1
        i = i+2
    elif(str_input[i:i+2] == "s=") :
        croatia_count+=1
        i = i+2

    elif(str_input[i:i+2] == "z=") :
        croatia_count+=1
        i= i+2
    else :
        i+=1
        croatia_count+=1
    
print(croatia_count)