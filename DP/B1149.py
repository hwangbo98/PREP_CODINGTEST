
N = int(input())

min_value = 0
prev_min_index = 0
current_min_index = 0
final_min = 0
result = []
for k in range(N) :
    result.append(list(map(int, input().split()))) # 리스트로 만들기

for j in range(1, N) :
    result[j][0] = min(result[j-1][1], result[j-1][2]) + result[j][0]
    result[j][1] = min(result[j-1][0], result[j-1][2]) + result[j][1]
    result[j][2] = min(result[j-1][0], result[j-1][1]) + result[j][2]

print(min(result[N-1][0],result[N-1][1],result[N-1][2]))

    



# if(k == 0) :
#         prev_min_index = result.index(min(result))
#         min_value += result[prev_min_index]
#     else :
#         current_min_index = result.index(min(result))
#         if prev_min_index == current_min_index :
#             del result[current_min_index]
#             final_min = result.index(min(result))
#             print(f'index of result = {final_min}')
            
#         else :
#             final_min = result.index(min(result))
#             print(f'index of result = {final_min}')
#         min_value += result[final_min]
#         prev_min_index = current_min_index

#     print(result[final_min])


# print(min_value)