# 백준 3062번 수 뒤집기 https://www.acmicpc.net/problem/3062
test_case = int(input())

num_list = [input() for i in range(test_case) ]
flip_list =[]

for num in num_list :
    flip_num = ""
    for i in range(len(num)-1,-1,-1) :
        flip_num+=num[i]

    flip_list.append(flip_num)

result = [str(int(num_list[i])+int(flip_list[i])) for i in range(len(num_list))]
print_result = []
for num in result :
    for i in range(len(num)) :
        if num[i] == num[len(num)-1-i] :
            true_false = True
        else :
            true_false = False
            break
    
    if true_false == True :
        print_result.append("YES")
    else :
        print_result.append("NO")

for i in print_result :
    print(i)
