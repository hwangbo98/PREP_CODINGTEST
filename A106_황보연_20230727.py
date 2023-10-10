#백준 3059번 등장하지 않는 문자의 합 https://www.acmicpc.net/problem/3059

alphabet = [chr(i) for i in range(65,91)]


start_to_end = 0
for k in alphabet :
    start_to_end+=ord(k)

test_case = int(input())
big_list = []
for i in range(test_case) :
    small_list=set(list(input()))
    #set(small_list)
    big_list.append(small_list)


result =[]
for word in big_list :
    sum_num = 0
    for alpha in word :
        if alpha in alphabet :
            sum_num+=ord(alpha)
        
    result.append(sum_num)

for j in result :
    print(start_to_end- j)