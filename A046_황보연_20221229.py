
count_person = int(input())

first_char = []
for x in range(count_person) :
    first_name = input()
    first_char.append(first_name[0])

list_set = list(set(first_char))
list_set.sort()
dict_count = {}
for i in list_set :
    dict_count[i] = first_char.count(i)
count_result = 0
for keys in dict_count.keys() :
    if dict_count[keys] >= 5 :
        print(keys,end="")
        count_result+=1

if(count_result==0) :
    print("PREDAJA")

