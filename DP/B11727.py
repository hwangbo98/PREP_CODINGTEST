
N = int(input())
tile = [0] * (N+1)

tile[0] = 1
tile[1] = 3

for k in range(2,N) :
    tile[k] = tile[k-1] + tile[k-2]*2

print(tile[N-1]%10007)