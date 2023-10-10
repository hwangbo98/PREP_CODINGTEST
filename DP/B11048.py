
N, M = map(int,input().split())

DP = [[0] * (M+1)] * (N+1)
candy = []
for k in range(N) :
    candy.append(list(map(int, input().split())))

for i in range(1, N+1) :
    for j in range(1, M+1) :
        DP[i][j] = max(DP[i-1][j-1], DP[i-1][j], DP[i][j-1]) + candy[i-1][j-1]

print(DP[N][M])