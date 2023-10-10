
test_case = int(input())

result = []
zero_floor = [i for i in range(1,15)]

result.append(zero_floor)

print(result)

for k in range(0,15) :
    new_append =[]
    sum_floor= 0
    for j in range(k) :
        sum_floor+=result[k][j]
    new_append.append(sum_floor)
    result.append(new_append)

print(result)