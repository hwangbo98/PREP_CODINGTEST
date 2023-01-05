import sys

input = sys.stdin.readline

def gcd(a,b) :
    while b >0 :
        a, b = b, a % b

    return a

def lcm(a,b,gcd_input) :
    return a*b // gcd_input ;
n_input = int(input())

for i in range(n_input) :
    a, b = map(int, input().split())
    gcd_ab = gcd(a,b)
    print(lcm(a,b,gcd_ab))

# print(gcd(4,6))

# print(3%4)