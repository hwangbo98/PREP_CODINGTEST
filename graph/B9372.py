
import sys

T = int(sys.stdin.readline())

for _ in range(T) :
    N, M = map(int, sys.stdin.readline().split())
    flight_plan = []
    for _ in range(M) :
        a, b = map(int, sys.stdin.readline().split())
        flight_plan.append((a,b))

    print(N-1)
# from collections import deque
# T = int(input())



# def bfs(N, flight) :
#     result = [0 for _ in range(N+1)]
#     total_cnt = [0 for _ in range(N+1)]
#     for k in range(1,N+1) :
#         visited = [False] * (N+1)

#         queue = deque([k])

#         visited[k] = True
#         cnt = 0
#         while queue :
#             n = queue.popleft()

#             for i in flight[n] :
#                 if not visited[i] :
#                     cnt+=1
#                     queue.append(i)
#                     visited[i] = True


#         total_cnt[k] = cnt
    
#     return total_cnt




# final_result = []
# for _ in range(T) :
#     N, M = map(int, input().split())
#     flight_plan = []
#     for _ in range(M) :
#         a, b = map(int, input().split())
#         flight_plan.append((a,b))
#     edit_flight_plan = [[] for _ in range(N+1)]
#     for a,b in flight_plan :
#         edit_flight_plan[a].append(b)
#         edit_flight_plan[b].append(a)

#     # print(edit_flight_plan)
#     # result = dfs(N, edit_flight_plan)
#     result = bfs(N, edit_flight_plan)
#     # print(min(result[1:]))
#     final_result.append(min(result[1:]))



# for val in final_result :
#     print(val)


# def dfs(N, flight ) :
#     result = [0 for _ in range(N+1)]
#     for k in range(1,N+1) :
#         stack = [k]
#         visited = []
#         count = 0
#         while stack : 
#             current = stack.pop()
#             for neighbor in edit_flight_plan[current] :
#                 if neighbor not in visited :
#                     count+=1
#                     print(neighbor)
#                     stack.append(neighbor)
            
#             visited.append(current)
#         # print('--------')
#         result[k] = count
    
#     return result



