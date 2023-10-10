from collections import deque

R, C = map(int, input().split())

micky = []

for _ in range(R) :
    a = [k for k in input()]
    micky.append(a)

# print(micky)
visited = [[0 for _ in range(C)] for _ in range(R)]
def bfs(x,y) :
    # direction = [(-1,0), (-1,1), (0,1), (1,1),
    #         (1,0), (1,-1), (0,-1), (-1,-1)
    #         ]
    sheep = 0
    wolf = 0
    direction = [(-1,0), (1, 0), (0,-1), (0,1)] # 상하좌우

    queue = deque()
    queue.append((x,y))
    # print(queue)
    # micky[x][y] == '.'
    if micky[x][y] == 'v' :
        wolf+=1
    elif micky[x][y] == 'o' :
        sheep+=1
    visited[x][y] = 1
    
    while queue :
        a, b = queue.popleft()
        # cnt+=1
        # print(f'a = {a}, b = {b}')
        # if cnt == 5 :
        #     break
        for i in range(4) :
            nx = a + direction[i][0]
            ny = b + direction[i][1]

            if nx < 0 or nx >= R or ny < 0 or ny >= C :
                continue

            if not visited[nx][ny] :
                if micky[nx][ny] == '.' :
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
                elif micky[nx][ny] == 'o' :
                # micky[nx][ny] = '.'
                # queue.append((nx,ny))
                # print(f' o : nx = {nx}, ny = {ny}')
                    queue.append((nx,ny))
                    visited[nx][ny] = 1     
                    sheep+=1
                elif micky[nx][ny] == 'v' :
                    # micky[nx][ny] = '.'
                    wolf+=1
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
            # print(f' v :nx = {nx}, ny = {ny}')
    # print(wolf, sheep)

    return wolf, sheep
    
wolf = 0
sheep = 0
total_wolf = 0
total_sheep = 0
for i in range(R) :
    for k in range(C) :
        if not visited[i][k] and micky[i][k] != '#' :
            wolf, sheep = bfs(i,k)
            if wolf >= sheep :
                # total_sheep += sheep
                total_wolf += wolf
            else :
                total_sheep += sheep

print(total_sheep,total_wolf)