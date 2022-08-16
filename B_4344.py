
test_case = int(input())

s_list = [input() for _ in range(test_case)] #예시로 n에 3넣어 3줄 입력받기(엔터로 구분)
#int_list = list(map(int, s_list))
ratio_person = []
for num in range (test_case) :
    count_num = 0
    int_list = [int(j) for j in s_list[num].split()]
    sum_score = sum(int_list)
    sum_score = sum_score - int_list[0] # test case 별 총 점수
    avg_score = float(sum_score/int_list[0])
    for k in int_list[1:] :
        if k > avg_score :
            count_num+=1
    #print(count_num)
    print(f"{round(float(count_num/int_list[0])*100,3):.3f}%")
