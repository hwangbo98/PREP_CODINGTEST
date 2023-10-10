import sys

N = int(sys.stdin.readline())

M = int(sys.stdin.readline())

parents = [0] * (N+1)

for i in range(N+1) :
    parents[i] = i

def find_parents(parents, x) :
    if parents[x] != x :
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

def union_parents(parents, a, b) :
    a = find_parents(parents, a) 
    b = find_parents(parents, b)

    if a < b :
        parents[b] = a
    elif a > b :
        parents[a] = b
    

edges = []
total_cost = 0

for i in range(M) :
    a, b, cost = map(int, input().split())

    edges.append((cost, a, b))

edges.sort()

for k in range(M) :
    cost, a, b = edges[k]

    if(find_parents(parents, a)!= find_parents(parents, b)) :
        union_parents(parents, a, b)    
        total_cost+=cost
    
print(total_cost)