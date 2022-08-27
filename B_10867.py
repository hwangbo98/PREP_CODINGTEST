test_case = int(input())

list_num = map(int, input().split())


result = list(set(list_num))
result.sort()
print(result)

count = 0
for i in result :
    if(count == len(result)) :
        print(i)
        
    print(i, end = " ")