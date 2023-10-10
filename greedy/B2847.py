N = int(input())

game_level = [int(input()) for _ in range(N)]

count = 0
for i in reversed(range(N-1)) :
    if game_level[i+1] <= game_level[i] :
        minus = game_level[i] - game_level[i+1] + 1
        game_level[i] = game_level[i] - minus
        count += minus
    
print(count)