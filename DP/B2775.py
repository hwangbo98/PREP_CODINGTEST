
t = int(input())
print_out = []
for k in range(t) :
    floor = int(input())
    ho = int(input())

    result = [j for j in range(1, ho + 1)]

    # print(result)

    for i in range(1,floor+1) :
        for v in range(1, ho) :
            result[v] += result[v-1]
        
        # print(f'{i}층 {result}')
    
    print_out.append(result[-1])



for res in print_out :
    print(res)