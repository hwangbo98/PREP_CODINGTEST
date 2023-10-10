import sys

sys.setrecursionlimit(10**6)
N = int(input())

# edges = []
nodes = [[] for _ in range(N+1) ]
for i in range(N-1) :
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

parents = [0 for _ in range(N+1)]

def recurssion_dfs(graph, vertex, visited) :
    for i in graph[vertex] :
        if not visited[i] :
            visited[i] = vertex
            recurssion_dfs(graph, i, visited)

recurssion_dfs(nodes, 1, parents)

for k in range(2, N+1) :
    print(parents[k])

# def dfs(nodes, root, N) :
#     stack = [root]
#     visited = []
#     parents = [ _ for _ in range(N+1)] 
#     while stack :
#         current = stack.pop()

#         for neighbor in nodes[current] :
#             if neighbor not in visited :
#                 stack.append(neighbor)
#             else :
#                 parents[current] = neighbor
        
#         visited.append(current)

    
#     # print(parents)
#     return parents

# parents = dfs(nodes,1, N)

# for k in range(2, N+1) :
#     print(parents[k])

# # print(parents)



