
# s = list(map(str, input().split())
s = list(input())

init = '1'
count = 0
for k in range(0,len(s)) :
    if init == '1' and s[k] == '0' :
        count+=1
    init = s[k]
init_1 = '0'
count_1 = 0
for j in range(0, len(s)) :
    if init_1 == '0' and s[j] == '1' :
        count_1+=1
    init_1 = s[j]
    
print(min(count,count_1))
