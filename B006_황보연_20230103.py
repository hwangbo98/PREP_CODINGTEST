# https://www.acmicpc.net/problem/1260 DFS와 BFS 백준 1260번

from collections import deque

def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end = ' ')

    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)


N, M, V = map(int, input().split())

# pair_list = []
graph = [[] for i in range(N+1)]
for pair in range(M) :
    # pair_list.append(list(map(int, input().split())))
    a,b = map(int, input().split())
    graph[a]+=[b]
    graph[b]+=[a]

for i in range(len(graph)) :
    graph[i].sort()

visited = [False] * (N +1)
visited1 = [False] * (N +1)
# print(graph)
dfs(graph, V, visited)
# print('\n')
print()
visited1[V] = True

queue = deque([V])

# while queue :
#     q = queue.popleft()
#     for k in pair_list[q] :
#         if visited[k] == False :
#             queue.append(k)
#             visited[k] = True

# print(sum(visited)-1)

print(V, end= ' ')
while queue :
    q = queue.popleft()
    for k in graph[q] :
        if visited1[k] == False :
            queue.append(k)
            print(k, end = ' ')
            visited1[k] = True
print()
# def dfs(graph, v, visited) :
#     visited[v] = True
#     print(v, end = ' ')

#     for nk in graph[v] :
#         if not visited[nk] :
#             dfs(graph, nk, visited)


