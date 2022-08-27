#백준 10814번 나이순 정렬 https://www.acmicpc.net/problem/10814
test_case = int(input())
info_people = {}

big_age_name = []
for i in range(test_case) :
    age_name = []
    age, name = input().split()
    age_name.append(int(age))
    age_name.append(name)
    big_age_name.append(age_name)

# for i in range(test_case) :
#     age, name = input().split()
#     info_people[name] = int(age)
# sorted_info = sorted(info_people.items(), key= lambda x : x[1])
# print(sorted_info)
big_age_name.sort(key=lambda x: x[0])
for age, name in big_age_name :
    print(age, name, sep=" ")