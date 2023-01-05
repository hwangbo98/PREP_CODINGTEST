# 백준 검증수 https://www.acmicpc.net/problem/2475
input_str = input()

list_input = input_str.split()
result = 0
for i in list_input :
    result += pow(int(i),2)

print(result%10)