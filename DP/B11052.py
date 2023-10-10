N = int(input())

pack = list(map(int, input().split()))
pack.insert(0,0)

R = [0 for _ in range(N+1)]

for k in range(1,N+1) :
    for j in range(1, k+1) :
        R[k] = max(R[k], pack[j] + R[k-j])

print(R[N])
    
# print(pack)

