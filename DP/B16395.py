N, K = map(int, input().split())

DP = []

for i in range(1, N +1) :
    r = [1] * i
    DP.append(r)

for k in range(2, N) :
    for j in range(1,k) :
        DP[k][j] = DP[k-1][j-1] + DP[k-1][j]
        # print(DP[k][j])
    # print('p')

print(DP[N-1][K-1])