
N = int(input())

pack = list(map(int, input().split()))
pack.insert(0,0)
DP = [1e9 for _ in range(N+1)]

for j in range(1,N+1) :
    DP[j] = pack[j]

# print(f'pack : {pack}, DP : {DP} ')


for i in range(1, N+1) :
    for k in range(1, i+1) :
        DP[i] = min(DP[i], DP[k] + pack[i-k])

print(DP[N])