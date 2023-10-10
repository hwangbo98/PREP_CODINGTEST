str_input = input()
result = []
for i in range(len(str_input)) :
    result.append(str_input[i:])

result.sort()

for i in result :
    print(i)
