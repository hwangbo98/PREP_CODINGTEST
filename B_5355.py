
result = []

case_num = int(input())

for i in range(case_num) :
    list_str = [x for x in input().split()]
    sum_int = 0
    for i in list_str :
        if i == '@' :
            sum_int*=3
        elif i == '%' :
            sum_int+=5
        elif i == '#' :
            sum_int-=7
        else :
            sum_int+=float(i)

    result.append(sum_int)
    list_str.clear()


for k in result :
    print("{:.2f}".format(k))