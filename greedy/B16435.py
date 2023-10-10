import sys

input = sys.stdin.readline

N, length_snake_bird = map(int, input().split())

height = list(map(int, input().split()))

height.sort()

for h in height :
    if h <= length_snake_bird :
        length_snake_bird+=1
    
print(length_snake_bird)
