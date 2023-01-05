#백준 보물 1026번 https://www.acmicpc.net/problem/1026
num_input = int(input())

a_input = list(map(int, input().split()))
b_input = list(map(int, input().split()))


a_input.sort()
b_input.sort(reverse=True)

result = 0

for i in range(num_input) :
    result += a_input[i] * b_input[i]

print(result)