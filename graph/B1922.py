import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

adj_mat = [[0]*(N+1) for _ in range(N+1)]
# print(adj_mat)
for _ in range(M) :
    a, b, cost = map(int, sys.stdin.readline().split())
    adj_mat[a][b] = cost

print(adj_mat)


