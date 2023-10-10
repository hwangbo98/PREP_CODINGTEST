T = int(input())

for _ in range(T) :
    N = int(input())
    Coin = list(map(int, input().split()))
    Coin.insert(0,0)

    M = int(input())
    
    DP = [[0] * (M+1) for i in range(N+1)]

    for i in range(N+1) :
        DP[i][0] = 1
    
    for j in range(1, N+1) :
        for k in range(1, M+1) :
            DP[j][k] = DP[j-1][k]
            if k-Coin[j] >= 0 :
                DP[j][k] += DP[j][k-Coin[j]]

    print(DP[N][M])

    