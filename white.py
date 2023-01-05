# -*- coding: utf-8 -*-
list1= ['책 먹는 여우','아낌없이 주는 나무','어린왕자','빨강 머리 앤','돈키호테','달러구트 꿈 백화점','아몬드','나의 라임 오렌지나무','이상한 나라의 엘리스','천로역정']
list2= ['프란치스카 비어만','쉘 실버스타인','앙투안 드 생텍쥐페리','루시 모드 몽고메리','미겔 데 세르반테스','이미예','손원평','J.M. 바스콘셀로스','루이스 캐롤','존 번연']
list3= ["책에 대한 사랑이 지나쳐 급기야는 책을 먹게 된 여우 이야기!『책 먹는 여우』는 책에 빠진 독자의 모습을 과장되었지만 일리있게 표현하고 있다. 여우 아저씨는 책을 너무나 좋아했다."," 『아낌없이 주는 나무』는 인생의 참된 가치가 무엇인지 일러주는 작품이다. 진정한 사랑이 무엇인가를 일깨워 주는 나무의 아름다운 이야기다. 소년을 향한 나무의 무조건적인 사랑은 읽는 독자의 가슴을 울린다.","다른 별에서 온 어린 왕자의 순수한 시선으로 모순된 어른들의 세계를 비추는 이 소설은, 꾸밈없는 진솔한 문체와 동화처럼 단순해 보이는 이야기 속에 삶을 돌아보는 깊은 성찰을 아름다운 은유로 녹여 낸 작품이다.","‘초록 지붕 집’에 실수로 입양된 고아 소녀가 엉뚱한 상상력과 긍정의 에너지로 어려움들을 돌파해 가는, 세계에서 가장 유쾌한 성장소설이다.","이 작품은 기사도 소설에 미쳐 세상을 떠돌며 악을 처단하고 약자를 구원하는 편력 기사가 되기로 결심한 돈 키호테와 어리숙한 종자 산초 판사의 엉뚱하면서도 흥미진진한 여정을 담은 모험 소설이다.","『달러구트 꿈 백화점』은 ‘무의식에서만 존재하는 꿈을 정말 사고 팔 수 있을까?’라는 기발한 질문에 답을 찾아가며, 꿈을 만드는 사람, 파는 사람, 사는 사람의 비밀스런 에피소드를 담고 있는 판타지 소설이다.","‘감정을 느끼지 못하는’ 소년의 특별한 성장 이야기로, 첫 장부터 강렬한 사건으로 시작해 다음 페이지가 궁금해지게 만드는 흡입력 강한 작품이다. 또한 타인의 감정에 무감각해진 ‘공감 불능’인 이 시대에 큰 울림을 주는 소설이다.","이 작품은 너무나 잘 알려진 성장소설이다. 감수성이 예민한 다섯 살 소년 '제제'를 통해 사랑의 문제, 인간 비극의 원초적인 조건, 인간과 사물 또는 자연의 교감, 어른과 아이의 우정 등을 잔잔한 어조로 이야기하고 있다.","이 작품은 시계를 차고 있는 토끼에게 끌려 신기한 나라에 들어간 앨리스의 모험이 펼쳐진다. 기이한 등장인물들과의 우연한 만남과 반복들이 재미를 더한다.","천로역정은 무거운 짐을 등에 진 '크리스천'이 아내와 자녀들을 떠나 '멸망의 도시'에서 '천성'에 이르기까지 겪는 고난을 그려내고 있다. 자신의 순례를 위협하는 함정과 유혹을 성경의 지혜로 극복해내는 '크리스천'을 통해 하나님의 은혜를 되새기는 인생길로 안내한다."]
list4= [False, False, False, False, False, False, False, False, False, False]

print('Welcome, this is Wonderland')
while(True) :
    
    print('='*40)
    for index in range(len(list1)):
        print(index+1,'',list1[index])
    print('='*40)

    while(True) :
        bk_num = int(input("choose a book by its number : "))
        if (bk_num > 0 and bk_num < 11) :
            print('='*40)
            print('Title:',list1[bk_num-1])
            print('Author:',list2[bk_num-1])
            print('Plot summary:',list3[bk_num-1])
            print('='*40)
            borrowed_Q= input('If you like to borrow this book, please enter b : ')
            if borrowed_Q == 'b' :
                if list4[bk_num-1] == False :
                    print("Sucessfully borrowed")
                    list4[bk_num-1] = True
                else :
                    borrowed_C = input("You have already borrowed this book. If you like to cancel it, please enter c : ")
                    if borrowed_C == 'c' :
                        print("Sucessfully canceled")
                    else :
                        print("Not canceled")
            else :
                print("Not borrowed")
            print('='*40)

            while(True) :
                back_y_n = input("Back to the list (y) or quit (q) : ") 
                if back_y_n == "y" :
                    while(True) :
                        choose_1_2 = input("1. All, 2. Not borrowed : ")
                        if choose_1_2 == "1" :
                            break;
                        elif choose_1_2 == "2" :
                            break

                        

                    if choose_1_2 == "1" :
                        break
                    elif choose_1_2 == "2" :
                        print('='*40)
                        for num in range(len(list1)) :
                            if list4[num]!=True :
                                print(num+1,'',list1[num])
                        print('='*40)
                        break

                elif back_y_n == "q" :
                    print('='*40)
                    print("Thank you for visiting us.")
                    borrow_count = list4.count(True)
                    print("You have borrowed ", borrow_count," books.")
                    for count_num in range(len(list4)) :
                        if list4[count_num] == True :
                            print(list1[count_num])
                    print("See you again!")
                    break

            if choose_1_2 == "1" :
                break
            if back_y_n == "q" :
                break


        else :
            print("Wrong number")

    if back_y_n == "q" :
        break


    
    

