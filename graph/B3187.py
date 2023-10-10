import sys
from collections import deque

R, C = map(int, input().split())
farm = []
# farm = [[k] for k in sys.stdin.readline().split()] for _ in range(R)]
for k in range(R) :
    small_farm = [j for j in input()]
    farm.append(small_farm)

# farm = [[k for k in input()] for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R) ]

# print(visited)
# print(farm)

def bfs(x, y) :
    direction = [(-1,0), (1,0), (0,-1), (0,1)]
    wolf = 0
    sheep = 0
    if farm[x][y] == "v" :
        wolf+=1
    elif farm[x][y] == "k" :
        sheep+=1
    visited[x][y] = 1
    queue = deque([(x,y)])

    while queue :
        a, b = queue.popleft()
        # print(f'a = {a} , b = {b}')
        for i in range(4) :

            x_new = a + direction[i][0]
            y_new = b + direction[i][1]
            if x_new < 0 or x_new >= R or y_new < 0 or y_new >= C :
                continue
            if not visited[x_new][y_new] :
                if farm[x_new][y_new] == "." :
                    visited[x_new][y_new] = 1 
                    queue.append((x_new,y_new))
                elif farm[x_new][y_new] == "v" :
                    visited[x_new][y_new] = 1
                    wolf+=1
                    queue.append((x_new,y_new))
                elif farm[x_new][y_new] == "k" :
                    visited[x_new][y_new] = 1
                    sheep+=1
                    queue.append((x_new,y_new))
                
    return wolf, sheep
    
wolf = 0
sheep = 0
total_wolf = 0
total_sheep = 0

for i in range(R) :
    for k in range(C) :
        if not visited[i][k] and farm[i][k] != '#' :
            wolf, sheep = bfs(i,k)
            # print(wolf, sheep)
            if wolf >= sheep :
                total_wolf+=wolf
            else :
                total_sheep+=sheep

print(total_sheep, total_wolf)