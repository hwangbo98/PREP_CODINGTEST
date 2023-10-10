test_case = int(input())

list_num = map(int, input().split())


result = list(set(list_num))
result.sort()

for i in result :
    print(i, end = " ")