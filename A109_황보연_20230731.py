#백준 벨트 10834번 https://www.acmicpc.net/problem/10834
test_case = int(input())

list_case =[]
result = 1
for i in range(test_case) :
    a, b, type_belt = map(int, input().split())
    #print(a, b, type_belt)
    if(type_belt == 0) :
        if(a==1) :
            result= result*a*b
        else :
            result= result//a*b
    
    else :
        if(a==1) :
            result = result*a*-b
        else :
            result = result//a*-b
        

if result < 0 :
    print("1 " + str(result*-1))
else :
    print("0 " + str(result))
# for i in range(test_case) :
#     list_by = list(map(int, input().split()))
#     list_case.append(list_by)

# for line in list_case :
#     for k in range(len(line)) :


