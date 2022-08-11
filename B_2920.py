
input_music = input()

list_music = [int(num) for num in input_music.split()]

count_asc = 0
for i in range(len(list_music)-1) :
    if(abs(list_music[i] - list_music[i+1]) == 1 ) :
        count_asc+=1

if(count_asc == 7 and list_music[0] == 1 ) :
    print("ascending")
elif(count_asc == 7 and list_music[0] == 8) :
    print("descending")
else :
    print("mixed")
