import sys
from collections import deque

N, M = map(int, input().split())
campus = [[k for k in input()] for _ in range(N) ]
visited = [[0 for _ in range(M)] for _ in range(N) ]
# for _ in range(N) :
#     # in_campus = []
#     campus.append(in_campus)

def bfs(x,y) :
    direction = [(-1,0), (1,0), (0,-1), (0,1)]

    queue = deque()

    queue.append([x,y])
    visited[x][y] = 1
    person = 0
    while queue :
        a, b = queue.popleft()


        for i in range(4) :
            nx = a + direction[i][0]
            ny = b + direction[i][1]

            if nx <0 or nx >= N or ny < 0 or ny >= M :
                continue

            if not visited[nx][ny] :
                if campus[nx][ny] == "O" :
                    queue.append([nx,ny])
                
                elif campus[nx][ny] == "P" :
                    queue.append([nx,ny])
                    person+=1
                
                visited[nx][ny] = 1

    return person

# def dfs
for i in range(N) :
    for j in range(M) :
        if not visited[i][j] and campus[i][j] == "I" :
            person = bfs(i,j)
            if person == 0 :
                print("TT")
            else :
                print(person)

# print(person)
                    


# print(visited)
# print(campus)