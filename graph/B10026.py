from collections import deque

N = int(input())


area = [[k for k in input()] for _ in range(N)]
visited = [[0 for k in range(N)] for _ in range(N)]

area_eyes = area
for j in range(N) :
    for k in range(N) :
        if area[j][k] == "R" :
            area[j][k] == "G"

color_area = {'R' : 0, 'G' : 0, 'B' : 0}
# print(visited)
def bfs(x, y) :
    direction = [(-1,0), (1,0), (0,-1), (0,1)] 

    # stack = []

    queue = deque()
    queue.append([x,y])

    # deque.append([x,y])

    visited[x][y] = 1
        
    # if area[x][y] == "R" :

    while queue :
        a, b = queue.popleft()
        # print(a,b)
        for i in range(4) :
            nx = a + direction[i][0]
            ny = b + direction[i][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= N :
                continue

            if not visited[nx][ny] and area[x][y] == area[nx][ny] :
                queue.append([nx,ny])
                visited[nx][ny] = 1
            
    color_area[area[x][y]] +=1

# def dfs(x, y) :
#     direction = [(-1,0), (1,0), (0,-1), (0,1)] 

for i in range(N) :
    for k in range(N) :
        if not visited[i][k] :
            bfs(i,k)
            # break

print(color_area)

        
    # stack.append()


