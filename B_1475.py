
str_input = input()
int_list = [int(i)+3 if i=="6" else int(i) for i in str_input]
dict_list = {}

for k in set(int_list) :
    if k == 9 and int_list.count(k)%2 == 1 :
        dict_list[k] = int_list.count(k)//2 + 1
    elif k==9 and int_list.count(k)%2 ==0 : 
        dict_list[k] = int_list.count(k)//2
    else :
        dict_list[k] = int_list.count(k)


max_value = max(dict_list, key = dict_list.get)

print(dict_list[max_value])

