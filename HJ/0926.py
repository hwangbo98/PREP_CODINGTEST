word = ['Apple', 'box', 'buzz', 'CANTUS', 'dish', 'knife', 'lady', 'pitch', 'stimulus', 'wish', 'wolf']

vowels = ['a', 'e', 'i', 'o', 'u', 'A','E','I','O','U']

for i in word:
    count = 0
    print(i,"은(는)", end=" ")
    for ii in i:
        if ii in vowels:
            count=count+1
            print(ii, end = ' ')
    
    print(count, '개', end =' ')