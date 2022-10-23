from collections import Counter
import sys

#https://www.acmicpc.net/problem/2108 백준 2108번 통계학, collections에서 counter 라는 library에 대해 알게 됨.
def mean_num(list_input, num) :
    
    return (round(sum(list_input)/num))

def median_num(list_input, num) :

    return list_input[num//2]

def fre_num(list_input, num) :
    dict_list = {}

    input_s  = Counter(list_input).most_common()
    if(len(input_s) == 1) :
        return input_s[0][0]
    else :
        if input_s[0][1] == input_s[1][1] :
            return input_s[1][0]
        else :
            return input_s[0][0]
    

def range_num(list_input, num) :
    list_input = sorted(list_input)

    if(num ==1) :
        return 0
    else :
        return (list_input[-1] - list_input[0])

num = int(sys.stdin.readline())

list_num = []

for i in range(num) :
    list_num.append(int(sys.stdin.readline()))


list_num.sort()

mean_res = mean_num(list_num, num)

median_res = median_num(list_num, num)

fre_res = fre_num(list_num, num)

range_res = range_num(list_num, num)


print(mean_res)
print(median_res)
print(fre_res)
print(range_res)