tem = int(input("오늘 온도를 입력하세요. "))
rain_or_not = input("비가 오나요? ")

if(tem>=30 and rain_or_not=="네") :
    print("오늘 날씨는 덥고 비가 온다.")
elif(tem>=30 and rain_or_not!="네") :
    print("오늘 날씨는 덥고 비는 안온다.")
elif(tem<30 and rain_or_not=="네") :
    print("오늘 날씨는 덥지 않고, 비는 온다.")
else :
    print("오늘 날씨는 덥지 않고, 비도 오지 않는다.")