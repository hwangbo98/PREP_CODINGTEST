
dict_score = {}
for i in range(8) :
    score = int(input())
    dict_score[i+1] = score

sorted_list = sorted(dict_score.items(), key = lambda item : item[1], reverse = True)

count = 0
result_sum = 0
sorted_keys = []
for keys, values in sorted_list :
    if(count==5) :
        break
    else :
        sorted_keys.append(keys)
        result_sum+=values

    count+=1

print(result_sum)
for i in sorted(sorted_keys) :
    print(i, end= " ")