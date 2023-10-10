# https://school.programmers.co.kr/learn/courses/30/lessons/12951
def solution(s):
    answer = []
    # s = s.lower()
    # s = s.capitalize()
    
    spl_list = s.split(' ')
    
    # answer = list(s)
    
    for k in spl_list :
        k = k.capitalize()
        answer.append(k)
    
#     for k, letter in enumerate(answer) :
#         if letter == ' ' :
#             ascil_num = ord(answer[k+1])
#             if  97<=ascil_num <=122 :
#                 ascil_num -=32
#                 answer[k+1] = chr(ascil_num)
                
    answer = " ".join(answer)
    
    return answer