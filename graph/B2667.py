import sys
from collections import deque

N = int(sys.stdin.readline())

apart = []

for _ in range(N) :
    one_d = list(int(k) for k in input())

    apart.append(one_d)


direction = [(-1,0), (1, 0), (0,-1), (0,1)] # 상하좌우

def bfs(graph, direction, x, y ) :
    queue = deque()
    queue.append((x,y))
    count = 1
    while queue :
        x, y = queue.popleft()
        graph[x][y] = 0
        for i in range(4) :
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N :
                continue;
            
            if graph[nx][ny] == 1 :
                count+=1
                queue.append((nx,ny))
                graph[nx][ny] = 0 

    # print(count)
    return count

cnt = []
for i in range(N) :
    for k in range(N) :
        if apart[i][k] == 1 :
            cnt.append(bfs(apart, direction, i, k))
# print(cnt.sort)
cnt.sort
print(len(cnt))
for k in cnt :
    print(k)