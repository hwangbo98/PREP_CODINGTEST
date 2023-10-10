
N = int(input())
T = []
P = []
# T.append(0)
# P.append(0)
DP = [0 for _ in range(N+1)]
for k in range(N) :
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)


for i in range(N-1, -1, -1) :
    if T[i] + i > N :
        DP[i] = DP[i+1]
    else :
        DP[i] = max(DP[i+1], DP[T[i] + i] + P[i])

print(DP[0])