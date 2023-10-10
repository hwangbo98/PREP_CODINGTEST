N = input()
poly = ["AAAA", "BB"]

dot_pos = []
for cnt, i in enumerate(N) :
    if i == '.' :
        dot_pos.append(cnt)
cnt_X = 0
X_cnt = []
for j in range(len(N)) :
    if j not in dot_pos :
        cnt_X+=1
    elif j in dot_pos and cnt_X == 0 :
        pass
    elif j in dot_pos and cnt_X != 0 :
        X_cnt.append(cnt_X)
        cnt_X = 0

if cnt_X!=0 :
    X_cnt.append(cnt_X)

str_list = []
for j in X_cnt:
    str_parse = ""
    while(j>0) :
        if j // 4 > 0 :
            str_parse+= poly[0] *(j//4)
            j = j%4
        elif j // 2 > 0 :
            str_parse+=poly[1] * (j//2)
            j = j%2
        else :
            print(-1)
            exit(0)
    str_list.append(str_parse)

# print(str_list)
str_sum = ""
cnt_sum = 0
a = 0
for k in range(len(N)) :
    if k in dot_pos :
        str_sum+="."
        cnt_sum = 0
    elif k not in dot_pos and cnt_sum == 0:
        str_sum+= str_list[a]
        cnt_sum+=1
        a +=1
print(str_sum)
