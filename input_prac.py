korean = int(input())
math = int(input())
english = int(input())
history = int(input())

subject ={}
subject['국어'] = korean
subject['수학'] = math

for i in subject.keys() :
    print(i)
    
total = korean+math+english+history

average = total/4

print(total, average)