def solution(a, b):
    answer = ''
    month_day = [31,29,31,30,31,30,31,31,30,31,30,31]
    sum = 0
    for i in range(1,a) :
        sum+= month_day[i-1]
    sum+=b
    print(sum)
    
    if sum %7 == 0 :
        return "THU"
    elif sum%7 == 1 :
        return "FRI"
    elif sum%7 == 2 :
        return "SAT"
    elif sum%7 == 3 :
        return "SUN"
    elif sum%7 == 4 :
        return "MON"
    elif sum%7 == 5:
        return "TUE"
    elif sum%7 == 6 :
        return "WED"