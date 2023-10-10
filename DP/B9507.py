n = int(input())

list_n = [int(input()) for k in range(n)]

koong_list = []

koong_list.append(1)
koong_list.append(1)
koong_list.append(2)
koong_list.append(4)

result = []

max_in_list = max(list_n)

for j in range(4,max_in_list+1) :
    value =  koong_list[j-1] + koong_list[j-2] + koong_list[j-3] + koong_list[j-4]
    koong_list.insert(j,value)

for k in list_n :
    result.append(koong_list[k])

for k in result :
    print(k)