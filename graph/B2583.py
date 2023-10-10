import sys

sys.setrecursionlimit(10000)

M, N, K = map(int, input().split())

result = [[0]*N for _ in range(M)]

for _ in range(K) :
    tl_x, tl_y, br_x, br_y =  map(int, input().split())
    for i in range(tl_y, br_y) :
        for j in range(tl_x, br_x) :
            result[i][j] = 1


def dfs(x, y, count) :
    result[y][x] = 1 # 방문했다고 표시함
    for dx, dy in direction :
        X, Y = x + dx, y + dy
        if (0 <= Y < M) and (0 <= X < N) and result[Y][X] == 0 :
            count = dfs(X, Y, count+1)

    return count


area = []
direction = [(0,1), (1,0), (0,-1), (-1,0)]

for y in range(M) :
    for x in range(N) :
        if(result[y][x] == 0) :
            area.append(dfs(x, y, count = 1))
print(len(area))
print(*sorted(area))