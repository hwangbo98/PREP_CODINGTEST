str_input = []
for i in range(10) :
    str_split = list(map(float, input().split()))
    
    for i in str_split :
        str_input.append(i)

for k in str_input :
    if k >=7.44 and k<=7.52 :
        print(k)