# https://school.programmers.co.kr/learn/courses/30/lessons/42889
# 실패율 카카오 2019 블라인드 코딩테스트
def solution(N, stages):
    answer = []
    fail_rate = {}
    count_person = len(stages)
    
    for i in range(1,N+1) :
        fail_rate[i] = stages.count(i)
    
    for key, value in fail_rate.items() :
        try :
            fail_rate[key] = value / count_person
            count_person-=value
        except ZeroDivisionError :
            fail_rate[key] = 0
        
    print(fail_rate)
    sorted_dict = sorted(fail_rate, key = lambda x: fail_rate[x], reverse = True)
    print(sorted_dict)
    return sorted_dict