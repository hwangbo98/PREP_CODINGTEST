from collections import deque

N, M = map(int, input().split())

user = [[] for _ in range(N+1)]
for _ in range(M) :
    A, B = map(int, input().split())
    user[A].append(B)
    user[B].append(A)

# print(user)

result = [1000000 for _ in range(N+1)]
# print(result)
# dic_count = {x:0 for x in range(N+1)}
def bfs_graph(N, user, visited,result) :
    
    for k in range(1, N+1) :
        total_cnt = 0
        visited = [False]*(N+1)
        queue = deque([k])
        # print(k)
        visited[k] = True
        count = 0
        dic_count = {x:0 for x in range(N+1)}
        dic_count[k] = 1


        while queue :
            len_queue = len(queue)
            n = queue.popleft()
            # print(n, end='')
            # count+=1
            for i in user[n] :
                if not visited[i] :
                    # print(f'n= {i}, cnt = {count}')
                    queue.append(i)
                    visited[i] = True
                    # total_cnt +=count
                    dic_count[i] = dic_count[n] + 1

        # result[k] = total_cnt
        for val in dic_count.values() :
            if val == 1 :
                pass
            else :
                count+=val
        
        count-=N-1
        # print(dic_count)
        result[k] = count
    
    print(result.index(min(result)))


visited = [False]*(N+1)

bfs_graph(N, user, visited,result)

# def stack_graph(N, user, result) :
#     for k in range(1, N+1) :
#         stack = [k]
#         visited = []
#         count = 0
#         total = 0
#         while stack :
#             current = stack.pop()
            
#             for neighbor in user[current] :
#                 print(f'neighbor : {neighbor}, count : {count}')
#                 count+=1
#                 if neighbor not in visited :
#                     # count+=1
#                     stack.append(neighbor)
                
#             visited.append(current)
        
#         result[k] = count

#     return result

# new_result = stack_graph(N, user, result)        

# print(new_result)