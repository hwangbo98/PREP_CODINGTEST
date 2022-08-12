#https://school.programmers.co.kr/learn/courses/30/lessons/12918
#문자열 다루기 프로그래머스

def solution(s):
    answer = True
    s_list = list(s)
    
    if(len(s_list) == 4 or len(s_list) == 6) :
        answer = True
        for k in s_list :
            if(ord(k) >=48 and ord(k) <=57) :
                pass
            else :
                answer = False
    else :
        answer = False
    return answer