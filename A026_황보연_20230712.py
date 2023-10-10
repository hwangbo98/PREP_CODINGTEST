
# https://school.programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    answer = True
    x = str (x)
    sum = 0
    for i in x :
        sum+= int(i)
    x = int (x)
    if x%sum == 0 :
        answer = True
    else :
        answer = False
        
    return answer