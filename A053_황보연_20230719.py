N_count = int(input())

str_list = [input() for i in range(N_count)]
stack = []
for x in str_list :
    if 'push' in x :
        space_index = x.find(' ')
        stack.append(x[space_index+1:])

    elif 'top' in x :
        if len(stack) == 0 :
            print('-1')
        else :
            print(stack[-1])
    
    elif 'size' in x :
        print(len(stack))

    elif 'empty' in x :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)

    elif 'pop' in x :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])
            del stack[-1]