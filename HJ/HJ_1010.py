input_str = input("문자열을 입력하세요 (10글자 이상만 가능): ")

# 문자열 변환
new_str = input_str.swapcase().replace(' ', '*')

print("변환 후:", new_str)

# 단어 분할
result=[]
# result = new_str.split('[a-z]')
start = 0
count = 0

for i in range(len(new_str)+1) :
    if i == len(new_str) :
        result.append(new_str[start:])
    else :
        if new_str[i].islower() :
            end = i 
            result.append(new_str[start:end])
            start = i 

print(new_str[0:1])
print("리스트:", result)