N = input()
dic_H = {}

for i in N :
    if not i in dic_H :
        dic_H[i] = 1
    else :
        dic_H[i]+=1

    # dic_H[i] +=1

sorted_dict = sorted(dic_H.items(), key = lambda item : item[0])

# print(sorted_dict)

cnt = 0
center = ""
for key, value in sorted_dict :
    if value % 2 != 0 :
        if center == "" :
            center = key
        else :
            print("I'm Sorry Hansoo")
            exit(0)

answer = ""
temp = ""

for key, value in sorted_dict :
    count = value // 2
    temp += key * count
    # print(value)
    dic_H[key] = int(value / 2)
answer += temp

if center != "" :
    answer+=center
answer += temp[::-1]

print(answer)