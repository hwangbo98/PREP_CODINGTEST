str_input = ""
str_list = []
dict_word ={}
moeum = ['a','e','i','o','u']
while(str_input != "end") :
    str_input = input()
    if(str_input == 'end') :
        break
    else :
        str_list.append(str_input)

for word in str_list :
    dict_word[word] = True

for word in str_list :
    if dict_word[word] == True :
        if ('a')  in word :
            dict_word[word] = True
        elif 'e' in word :
            dict_word[word] = True
        elif 'i' in word :
            dict_word[word] = True
        elif 'o' in word :
            dict_word[word] = True
        elif 'u' in word :
            dict_word[word] = True
        else :
            dict_word[word] = False
        
        if dict_word[word] == True :
            count = 0
            for i in range(len(word)-2) :
                if (((word[i] in moeum) and (word[i+1] in moeum) and (word[i+2] in moeum))) :
                    dict_word[word] = False
                    #print('in moeum ' + word + str(count))
                elif (((word[i] not in moeum) and (word[i+1] not in moeum) and (word[i+2] not in moeum))) :
                    dict_word[word] = False
                    #print('not in moeum ' + word + str(count) )
                
            if dict_word[word] == True :
                for i in range(len(word)-1) :
                    if((word[i] == word[i+1]) and (word[i] == 'e') or (word[i] == 'o') ) :
                        dict_word[word] = True
                    elif((word[i] == word[i+1])) :
                        dict_word[word] = False
                # elif  in moeum :
                #     dict_word[word] = False
                #     print('in moeum ' + word)
            # if dict_word[word] == True :

            #     for k in range(len(word) -1) :
            #         if word[k] == word[k+1]  :
            #             dict_word[word] = True
            #         else :
            #             dict_word[word] = False
    

for keys, values in dict_word.items() :
    if values == True :
        print("<" + keys +"> " + "is acceptable.")
    else :
        print("<" + keys + "> " + "is not acceptable.")