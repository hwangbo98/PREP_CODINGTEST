import sys
from collections import deque
sys.setrecursionlimit(10000)

def bfs(x, y):
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    direction = [(-1,0), (-1,1), (0,1), (1,1),
                (1,0), (1,-1), (0,-1), (-1,-1)
                ]

    map_2d[x][y] = 0
    q = deque()
    q.append([x, y])
    while q:
        a, b = q.popleft()
        for i in range(8):
            nx = a + direction[i][0]
            ny = b + direction[i][1]
            if 0 <= nx < h and 0 <= ny < w and map_2d[nx][ny] == 1:
                map_2d[nx][ny] = 0
                q.append([nx, ny])

# cnt_list = []

def dfs(x,y) :
    dx = [1, 1, -1, -1, 1, -1, 0, 0]
    dy = [0, 1, 0, 1, -1, -1, 1, -1]
    direction = [(-1,0), (-1,1), (0,1), (1,1),
                (1,0), (1,-1), (0,-1), (-1,-1)
                ]
    map_2d[x][y] = 0

    for i in range(8) :
        nx = x + direction[i][0]
        ny = y + direction[i][1]
        if 0 <= nx < h and 0 <= ny < w and map_2d[nx][ny] == 1 :
            dfs(nx,ny)

while (True) :
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0 :
        break
    map_2d = []
    for _ in range(h) :
        map_2d.append(list(map(int, sys.stdin.readline().split())))

    # print(map_2d)

    direction = [(-1,0), (-1,1), (0,1), (1,1),
                (1,0), (1,-1), (0,-1), (-1,-1)
                ]


    cnt = 0
    for i in range(h) :
        for k in range(w):
            if map_2d[i][k] == 1 :
                # dfs(i,k)
                bfs(i,k)
                cnt+=1

    # cnt_list.append(cnt)
    print(cnt)
    