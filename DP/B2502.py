
D, K = map(int, input().split())

fib = [1, 1]

for k in range(2, D+1) :
    fib.append(fib[k-1] + fib[k-2])

A_cef, B_cef = fib[D-3], fib[D-2]


for A in range(1, K // A_cef + 1) :
    rest = K - (A * A_cef)
    if rest%B_cef  == 0 :
        B = rest // B_cef
        print(f'{A}\n{B}')
        break
