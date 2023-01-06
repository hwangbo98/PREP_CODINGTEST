# https://www.acmicpc.net/problem/1260 DFS와 BFS 백준 1260번

from collections import deque




N, M, V = map(int, input().split())

graph = [[] for i in range(N+1)]
for pair in range(M) :
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


