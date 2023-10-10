N = int(input())

RGB = [list(map(int, input().split())) for _ in range(N)]

ans = I = 1e9

for k in range(3) :
    dp = [[I,I,I] for _ in range(N)]

    dp[0][k] = RGB[0][k]

    for i in range(1, N) :
        dp[i][0] = RGB[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = RGB[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = RGB[i][2] + min(dp[i-1][0], dp[i-1][1])

    for j in range(3) :
        if k!=j :
            ans = min(ans, dp[-1][j])

print(ans)


