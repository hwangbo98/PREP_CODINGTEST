# https://www.acmicpc.net/status?user_id=hwangbo98&problem_id=1302&from_mine=1
# 백준 1302번 

length_int = int(input())
dict_book = {}
sorted_dict = {}
list_book = [input() for k in range(length_int)]
rm_dup = list(set(list_book))

for k in rm_dup :
    dict_book[k] = list_book.count(k)

sorted_dict = sorted(dict_book.items(), key=lambda x : (-x[1] , x[0]))

print(sorted_dict[0][0])
