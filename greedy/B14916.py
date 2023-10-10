N = int(input())

count_5 = N // 5
# print(count_5)
while(True) :
    new_N = N
    if not count_5 == 0 :
        new_N -= (count_5 * 5 )
        # print(f' N = {N}')
        if new_N%2 == 0 :
            count_2 = new_N // 2
            print(count_5 + count_2)
            break
        else :
            count_5-=1

    elif count_5 == 0 :
        if new_N%2 == 0 :
            count_2 = new_N //2
            print(count_2)
            break
        else :
            print(-1)
            break



        