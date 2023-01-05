from collections import deque

def dfs(graph, v, visited) :
    visited[v] = True
    #print(v, end = ' ')

    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)


computer_N = int(input())
pair_com = int(input())

# pair_list = []
pair_list = [[] for i in range(computer_N+1)]
for pair in range(pair_com) :
    # pair_list.append(list(map(int, input().split())))
    a,b = map(int, input().split())
    pair_list[a]+=[b]
    pair_list[b]+=[a]


visited = [False] * (computer_N +1)

dfs(pair_list, 1, visited)
# visited[1] = True

# queue = deque([1])

# while queue :
#     q = queue.popleft()
#     for k in pair_list[q] :
#         if visited[k] == False :
#             queue.append(k)
#             visited[k] = True

print(sum(visited)-1)

