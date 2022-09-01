#백준 3000번 버스 9546번 https://www.acmicpc.net/problem/9546
import math

test_case = int(input())

list_input = [int(input()) for i in range(test_case)]
print_out =[]
for num in list_input :
    result =0
    for i in range(num) :
        result = result+ math.pow(2,i)
    print_out.append(int(result))

for i in print_out :
    print(i)