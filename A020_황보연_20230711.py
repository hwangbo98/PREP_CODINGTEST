#백준 2455 지능형 기차 https://www.acmicpc.net/problem/2455
in_train = []
out_train = []
result = []
for i in range(4) :
    a,b = map(int, input().split())
    in_train.append(a)
    out_train.append(b)

result_sum = 0

for i in range(len(in_train)) :
    result_sum = result_sum + (out_train[i] - in_train[i]) 
    result.append(result_sum)
    
print(max(result))
