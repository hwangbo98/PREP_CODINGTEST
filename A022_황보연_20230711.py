#백준 1267번 핸드폰요금 https://www.acmicpc.net/problem/1267
int_input = int(input())

seconds_list = list(map(int, input().split()))

Y_shares=0
Y_remainder = 0
M_shares=0
M_remainder = 0
Y_standard = 30
M_standard = 60
Y_total=0 
M_total = 0

for i in seconds_list :

    Y_shares = i // Y_standard
    Y_remainder = i % Y_standard
    M_shares = i // M_standard
    M_remainder = i % M_standard
    #########
    Y_total += Y_shares * 10
    M_total += M_shares * 15
   
    Y_total+=10


    M_total+=15

if Y_total > M_total :
    print("M " + str(M_total))
elif M_total > Y_total :
    print("Y " + str(Y_total))
elif Y_total == M_total :
    print("Y M " + str(Y_total)  )
