

N = int(input())

loaf = [int(input()) for _ in range(N) ]

loaf.sort()

final = [] 

for cnt, k in enumerate(loaf) :
    final.append((len(loaf) - cnt) * k)
print(max(final))
