seats = int(input())

info_of_seats = input()

i = 0
list_of_seats = []
# print(len(info_of_seats))
while(i<=len(info_of_seats)-1) :
    if info_of_seats[i] == 'S' :
        list_of_seats.append(info_of_seats[i])
        i+=1
    else :
        list_of_seats.append(info_of_seats[i] + info_of_seats[i+1])
        i+=2
# print(list_of_seats.count('S'), list_of_seats.count('LL'))

count_cup_holder = list_of_seats.count('S')+ 1 + list_of_seats.count('LL')

print(min(seats, count_cup_holder))

