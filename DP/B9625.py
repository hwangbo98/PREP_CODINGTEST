
K = int(input())
DP = [0 for _ in range(K+1)]
DP[0] = (1,0)
DP[1] = (0,1)

for k in range(2, K+1) :
    a = DP[k-2]
    b = DP[k-1]

    DP[k] = (a[0] + b[0], a[1] + b[1])

print(DP[K][0], DP[K][1])    



