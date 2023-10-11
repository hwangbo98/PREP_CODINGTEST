N = int(input())

vote_result = [int(input()) for _ in range(N)]


count = 0

while(True) :
    voted_first_now = vote_result.index(max(vote_result))
    indices = [index for index, item in enumerate(vote_result) if item == max(vote_result)]
    if (len(indices) == 1 and voted_first_now == 0 ) :
        break
    elif (len(indices) !=1) :
        vote_result[indices[1]] -=1
        vote_result[0] +=1
        count+=1
    else :
        vote_result[voted_first_now] -=1
        vote_result[0] +=1
        count+=1



print(count)
