
str_input = input()
for word in str_input :
    if word == 'A' or word =='B' or word=='C' :
        strToint = ord(word) +23
    else :
        strToint = ord(word) -3

    print(chr(strToint), end="")
    