
A = input().split()

min_v = []
max_v = []
for k in A :
    min_v.append(int(k.replace('6','5')))
    max_v.append(int(k.replace('5','6')))


print(sum(min_v), sum(max_v))



