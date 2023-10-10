
N = int(input())
result = []
sorted_result = []
for k in range(N) :
    list_a = list(map(int, input().split(" ")))
    result.append(list_a)

# print(result)    

for k in range(len(result)) :
    sorted_result.append(sorted(result[k], reverse=True))

for res in sorted_result :
    print(res[2])
# print(sorted_result)