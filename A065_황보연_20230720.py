#백준 11650번 좌표 정렬하기 https://www.acmicpc.net/status?user_id=hwangbo98&problem_id=11650&from_mine=1
N_case = int(input())
x_y_list = []
for i in range(N_case) :
    x_y_list_ins = list(map(int, input().split()))
    x_y_list.append(x_y_list_ins)
x_y_list.sort()

for x, y in x_y_list :
    print(x, y)
