import sys
from collections import deque

def bfs(graph, direction, x, y) :
    queue = deque()
    queue.append((x,y))

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + direction[i][0]
            ny = y + direction[i][1]

            if 0<= nx < N and 0<= ny < M and graph[nx][ny] == 1 :
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1


    return graph[N-1][M-1]

N, M = map(int, sys.stdin.readline().split())

miro = []

for _ in range(N) :
    # one_d = list(map(int, input().split()))
    one_d = [int(k) for k in input()]
    # print(one_d)
    miro.append(one_d)

direction = [(-1,0), (1, 0), (0,-1), (0,1)] # 상하좌우

print(bfs(miro, direction, 0, 0))

# print(miro)
