# kor = int(input("국어 점수를 입력하세요."))
# math = int(input("수학 점수를 입력하세요."))
# eng = int(input("영어 점수를 입력하세요."))

# total = kor + math + eng
# avg = total/3

# print("국어 점수 : ", kor)
# print("수학 점수 : ", math)
# print("영어 점수 : ", eng)
# print("총 점수 : ", total)
# print("평균 점수 : ", avg)

# school = input("재학 중인 학교를 입력하세요. ")

# if school == "동지여고" :
#     print("동지여고에 다니시네요.")


#조건문 실습2

# tem = int(input("오늘 온도를 입력하세요. "))

# if tem >= 30 :
#     print("오늘 날씨는 더워요.")
# tem = int(input("오늘 온도를 입력하세요. "))

# if tem >= 30 :
#     print("오늘 날씨는 더워요.")

# else :
#     print("오늘은 덥지 않아요.")


# school = input("재학 중인 학교를 입력하세요 : ")

# #if not school == "동지여고" :
# if school != "동지여고" :
#     print("동지여고에 안다니시네요.")
# else :
#     print("동지여고에 다니시네요.")

# tem = int(input("오늘 온도를 입력하세요. "))
# rain = input("비가 오나요? ")

# if tem >= 30 and rain == "네" :
#     print("오늘 날씨는 덥고 비가 와요.")
# else :
#     print("오늘 날씨는 안덥거나 비가 안와요. 아니면 둘 다이거나")


# year = int(input())
# if year%4 ==0 and (year%100!=0 or year%400 ==0) :
#     print('윤년입니다.')
# else :
#     print('윤년이 아닙니다. ')


# print('-' * 40)
# print('달러($)'.rjust(8),   "원화(원)".rjust(8),   '유로(€)'.rjust(8))
# print('-' * 40)

# dollar = 10

# while dollar < 101:
#     won = dollar * 1410  # 원화 계산
#     euro = round(dollar * 0.99, 1)  # 유로 계산 (소숫점 첫째자리까지 표시)
    
#     print(str(dollar).rjust(10) , str(won).rjust(10), str(euro).rjust(10))
            
#     dollar += 10
    
# print('-' * 40)

# str_name = "String is very hard!!"

# print(str_name.center(30,'='))
# print(str_name.ljust(30, '='))
# print(str_name.rjust(30, "="))

# import random

# coin = random.randrange(0, 1)
# choice = int(input("동전이 앞면일까요? 뒷면일까요? (0:앞면, 1:뒷면) :"))

# if coin == choice:
#   print("적중 / 정답은 : ", coin)
# else:
#   print("아쉽네요. 틀렸습니다. / 정답은 : ", coin)

# import random

# RCP = ["바위", "가위", "보"]
# RCP = random.choice(RCP)

# user_RCP = input("바위, 가위, 보 : ")

# if RCP == user_RCP:
#   print("비겼습니다.")
#   print("computer : ", RCP, " VS ", "You : ", user_RCP)
# else:
#   if (RCP == '가위' and user_RCP =='바위') or (RCP == '바위' and user_RCP =='보') or (RCP == '보' and user_RCP =='가위'):
#     print("이겼습니다.")
#     print("computer : ", RCP, " VS ", "You : ", user_RCP)
#   elif (RCP == '가위' and user_RCP =='바위') or (RCP == '바위' and user_RCP =='가위') or (RCP == '보' and user_RCP =='가위'):
#     print("졌습니다.")
#     print("computer : ", RCP, " VS ", "You : ", user_RCP)


# 1. random 함수로 컴퓨터가 무작위로 가위바위보 중 하나 선택
# 2. 사용자가 가위바위보 중 하나를 입력하여
# 3. 컴퓨터와 가위바위보 대결

import random
import time 

w = ["cat","dog","fox","monkey","panda","frog","snake","wolf"]
n=1

print("[타자게임] 준비되면 엔터!")
input()
start = time.time() # 현재 시간을 구하는 함수 

q = random.choice(w) # w중에서 아무거나 하나를 뽑는 함수
for n in range(1, 6):
  print("*문제", n)
  print(q)
  x=input("=>")
  if q==x:
    print("통과!")
    q=random.choice(w)
  else:
    print("오타! 다시 도전!")

end = time.time()
et = end-start
print(f"타자 시간: {et:.3f} 초")