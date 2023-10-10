from collections import deque

test_case = int(input())

for _ in range(test_case) :
    count_of_wood = int(input())
    height_of_wood = list(map(int, input().split()))
    height_of_wood.sort(reverse=True)
    queue = deque()
    for cnt, height in enumerate( height_of_wood ):
        if cnt % 2 == 0 :
            queue.append(height)
        else :
            queue.appendleft(height)

    # print(queue)
    temp = 0
    for j in range(count_of_wood-1) :
        diff_adj_wood = abs(queue[j] - queue[j+1])
        if  diff_adj_wood > temp :
            temp = diff_adj_wood

    print(temp) 
    
