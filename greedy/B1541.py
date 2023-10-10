
N = input().split('-')
new = []
for i in N :
    # sum = 0
    K = list(map(int, i.split("+")))
    # print(sum(K))    
    new.append(sum(K))

# print(new)
sum = new[0]
for k in range(1, len(new)) :

    sum-=new[k]

print(sum)

