
test_case = int(input())
list_case = []
score_list = []
for i in range(test_case) :
    str_input = input()
    if(len(str_input) > 80 ) :
        pass
    else :
        list_case.append(str_input)

for OX in list_case :
    result = 0
    count = 0
    for split_OX in OX :
        if split_OX == "O" :
            count+=1
            result+=count
        elif split_OX == "X" :
            count=0
            result+=count
    
    score_list.append(result)

for i in score_list :
    print(i)
