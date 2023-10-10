V, E = map(int, input().split())

parents = [0] * (V+1)

for i in range(1, V+1) :
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

for _ in range(E) :
    a, b, cost = map(int, input().split())
    edges.append((cost,a,b))

edges.sort()

for i in range(E) :
    cost, a, b = edges[i]

    if find_parents(parents, a) != find_parents(parents, b) :
        union_parents(parents, a, b)
        total_cost += cost
    
print(total_cost)