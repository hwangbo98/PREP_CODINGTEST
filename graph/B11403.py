N = int(input())

adj_mat = [input().split() for _ in range(N)]

new_adj_mat = []

for i in range(N) :
    for j, k in enumerate(adj_mat[i]) :
        if k == '1' :
            new_adj_mat.append((i,j))

# print(new_adj_mat)

final_adj_mat = [[] for _ in range(N)]
for one in new_adj_mat :
    final_adj_mat[one[0]].append(one[1])

# print(final_adj_mat)

result = [[0]*N for _ in range(N)]
print('-----------------------')

def stack_graph(N, final_adj_mat, result) :
    for k in range(N) :
        stack = [k]
        vst_vert = []
        while stack :
            current = stack.pop()
            for neighbor in final_adj_mat[current] :
                result[k][neighbor] = 1
                if neighbor not in vst_vert :
                    stack.append(neighbor)
            
            vst_vert.append(current)
    
    return result

final_result = stack_graph(N, final_adj_mat, result)

for j in final_result :
    for z in j :
        print(z, end=' ')
    print( )

