
N = int(input())

triangle = []

for k in range(N) :
    triangle.append(list(map(int, input().split())))

for j in range(1, N) :
    triangle[j][0] += triangle[j-1][0] 
    triangle[j][len(triangle[j]) - 1] += triangle[j-1][len(triangle[j]) - 2] 
    for i in range(1, len(triangle[j]) - 1) :
        triangle[j][i] += max(triangle[j-1][i-1], triangle[j-1][i])

print(max(triangle[-1]))