
N = int(input())


for _ in range(N) :
    coin = {25 : 0, 10 : 0, 5 : 0, 1 :0}
    remainder = int(input())

    for i in coin.keys() :
        coin_count = remainder // i 
        remainder -= coin_count*i
        coin[i] = coin_count

    for k in coin.values() :
        print(k, end = ' ')

