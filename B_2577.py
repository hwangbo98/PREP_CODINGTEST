#백준 2577번 숫자의 갯수 https://www.acmicpc.net/problem/2577

a = int(input())
b = int(input())
c = int(input())

result = str(a*b*c)

for num in range(10) :
    print(str(result.count(str(num))))

    


