num1 = int(input())
num2 = int(input())


if num1 <= 0 or num2 <= 0 or num1 == num2 :
    print('입력 에러입니다.')

else :
    start = num1 
    end = num2 
    sum = 0
    count = 0
    if start > end : 
        for i in range(start, end - 1, -1) :
            if(count%2==0) :
                if i != end :
                    print(i,'-',end=' ')
                else :
                    print(i, end = ' ')
                sum+=i
            else :
                if i != end :
                    print(i,'+',end=' ')
                else :
                    print(i, end = ' ')
                sum-=i
            count+=1
        print('= ',sum)
    else :
        for i in range(start, end + 1) :
            if(count%2==0) :
                if i != end :
                    print(i,'-',end=' ')
                else :
                    print(i, end = ' ')
                sum+=i
            else :
                if i != end :
                    print(i,'+',end=' ')
                else :
                    print(i, end = ' ')
                sum-=i
            count+=1
        print('=',sum)


