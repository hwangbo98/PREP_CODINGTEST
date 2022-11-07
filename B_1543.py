import re
doc = input()

word = input()

len_word = len(word)
i = 0

count = 0
for m in re.finditer(word, doc) :
    count+=1

print(count)
    #print(word, m.start(), m.end())
# count = 0

# while(i < len(doc) - len(word)) :
#     if doc[i:i+len(word)] == word :
#         count+=1
#     else :
#         pass
#     i+=len(word)
    


# print(count)

