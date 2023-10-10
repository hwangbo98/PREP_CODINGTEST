N, M = map(int, input().split())

# print(N, M)

DNA = [input() for _ in range(N)]
Hamming_distance = 0
result_DNA = ""
for i in range(M) :
    DNA_count = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0  }
    for j in range(N) :
        DNA_count[DNA[j][i]] +=1
    
    dominant_dna = max(DNA_count, key=DNA_count.get)
    result_DNA+=dominant_dna
    Hamming_distance+= (N - DNA_count[dominant_dna])

print(result_DNA)
print(Hamming_distance)