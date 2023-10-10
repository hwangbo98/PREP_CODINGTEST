N = int(input())

# for k in range(N
Result = [1] * N

A = list(map(int, input().split()))

for k in range(1, N) :
    for j in range(k) :
        if A[j] > A[k] :
# print(A)

# for cnt, k in enumerate(A) :
#     # print(f' main_num = {k}')
#     R = []
#     for j in range(cnt+1, N) :
#         diff = k - A[j]
#         # print(f'diff = {diff}')
#         # print(f' A[j] = {A[j]}')
        
#         if diff <= 0 :
#             count = 0
#             pass
#         else :
#             value = A[j]
#             count = 2
#             for i in range(j+1, N) :
#                 # print(f' A[i] = {A[i]}')
#                 if value - A[i] == diff :
#                     value = A[i]
#                     count+=1
        
#         R.append(count)
#         # print(R)
    
#     Result.append(R)
            

            
# print(max(max(Result)))

